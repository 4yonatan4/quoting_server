from .xlsx_utils import xlsx_to_df
import pandas as pd


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class QuotationRequest:
    def __init__(self, request):
        self.term = request.get('term', None)
        self.coverage = request.get('coverage', None)
        self.age = request.get('age', None)
        self.height = request.get('height', None)
        self.weight = request.get('weight', None)
        self.health_class = request.get('health_class', None)
        self.rate = request.get('rate', None)
        self.price = request.get('price', None)

    def create_quotation(self):
        # Find health class
        self.health_class = HealthClassTable().find_health_class(self)
        # Find rate
        self.rate = RatesTable().find_rate(self)
        self.calc_price()
        return self.build_response()

    def calc_price(self):
        a = int(self.coverage)
        b = float(self.rate)
        # self.price = float("{:.3f}".format(((self.coverage / 1000) * self.rate)))

    def build_response(self):
        return {
            "price": self.price,
            "health-class": self.health_class,
            "term": self.term,
            "coverage": self.coverage
        }


# class Table(metaclass=Singleton):
#
#     def __init__(self):
#         self.health_class_df = xlsx_to_df(self.HEALTH_CLASS_TABLE)


class HealthClassTable(metaclass=Singleton):
    HEALTH_CLASS_TABLE = './quotation/static/Health Class table.xlsx'

    def __init__(self):
        self.health_class_df = xlsx_to_df(self.HEALTH_CLASS_TABLE)
        pass

    def find_health_class(self, quotation_request):
        height, weight = quotation_request.height, quotation_request.weight
        # split height to foot and inch
        height_foot, height_inch = height.split()[0] + '\'', height.split()[2] + '\"'
        # find a row with height_foot & height_inch
        for index, row in self.health_class_df.iterrows():
            if (row[0], row[1]) == (height_foot, height_inch):
                if row['Preferred Plus'] <= int(weight) < row['Preferred']:
                    return 'Preferred Plus'
                elif row['Preferred'] <= int(weight) < row['Standard Plus']:
                    return 'Preferred'
                elif row['Standard Plus'] <= int(weight) < row['Standard']:
                    return 'Standard Plus'
                elif row['Standard'] <= int(weight) < row['Declined']:
                    return 'Standard'
                else:
                    return 'Declined'


class RatesTable(metaclass=Singleton):
    RATES_TABLE = './quotation/static/Rates-table.xlsx'

    def __init__(self):
        self.rates_df = xlsx_to_df(self.RATES_TABLE)
        self.coverage_tables = self.create_coverage_tables()
        pass

    def create_coverage_tables(self):
        first_range = self.rates_df.iloc[:, :6]
        second_range = pd.concat([self.rates_df.iloc[:, :2], self.rates_df.iloc[:, 6:10]], axis=1, ignore_index=True)
        third_range = pd.concat([self.rates_df.iloc[:, :2], self.rates_df.iloc[:, 10:]], axis=1, ignore_index=True)
        first_range = (first_range.rename(columns=first_range.iloc[0])).iloc[1:, :]
        second_range = (second_range.rename(columns=second_range.iloc[0])).iloc[1:, :]
        third_range = (third_range.rename(columns=third_range.iloc[0])).iloc[1:, :]
        return {
            '100-249': first_range,
            '250-499': second_range,
            '500-999': third_range,
        }

    def find_rate(self, quotation_request):
        # find coverage table
        coverage_table = self.find_coverage_table(quotation_request.coverage)
        for index, row in coverage_table.iterrows():
            if (row[0], row[1]) == (quotation_request.term, quotation_request.age):
                return row[quotation_request.health_class]

    def find_coverage_table(self, coverage):
        for k, v in self.coverage_tables.items():
            values = k.split("-")
            if int(values[0]) * 1000 <= int(coverage) <= int(values[1]) * 1000:
                return v
        raise ValueError(f"We don't support this coverage value: {coverage}")
