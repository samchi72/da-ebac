import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico_gasolina.set(title='Preço da gasolina nos 10 primeiros dias de Julho de 2021', xlabel='dia', ylabel='preço')
  plt.savefig('gasolina.png')