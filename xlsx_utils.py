import pandas as pd


def xlsx_to_df(xlsx_file):
    df = pd.read_excel(xlsx_file, engine='openpyxl')
    return df


df = xlsx_to_df('Rates-table.xlsx')
df.drop(df.filter(regex="Unname"),axis=1)
print(df['coverage'])

