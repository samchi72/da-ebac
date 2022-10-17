import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('darkgrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico_gasolina.set(title='Gasoline prices in São Paulo on the first 10 days of July 2021', xlabel='day', ylabel='price')
  plt.savefig('gasolina.png')