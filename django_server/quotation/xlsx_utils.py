import pandas as pd


def xlsx_to_df(xlsx_file):
    df = pd.read_excel(xlsx_file, engine='openpyxl')
    return df
