import plotly.express as px
import pandas as pd

#DataFrame de vou de avião
aviao_df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv')

#excluindo linhas e colunas nula
aviao_df=aviao_df.dropna(how='all', axis=1)

#trocando nome das colunas
aviao_df.columns=['Anos','Meses','Passageiros']

#agruoando por ano e mês
aviao_df=aviao_df.groupby(['Anos','Meses'],as_index=False,sort=False).sum()

#criando grafico
grafAvi=px.line(aviao_df,x='Meses',y='Passageiros',color='Anos')
grafAvi.show()



