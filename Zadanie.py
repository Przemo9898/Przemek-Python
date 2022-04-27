import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx', header=0)
lista = df['Rok'].unique()
grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
wykres = grupa.plot(xticks=lista, figsize=(10, 6))
wykres.tick_params(axis='x', labelrotation=0)
plt.show()
