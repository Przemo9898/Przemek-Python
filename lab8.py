import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

print(df[df['Liczba'] > 1000])
print(df[df['Imie'] == 'PRZEMYSŁAW'])
print(df[(df['Rok'] > 2005) & (df['Rok'] > 2000))].agg({'Liczba': ['sum']}))