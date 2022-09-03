import numpy as np
import pandas as pd
import plotly.express as px
#dataframe de um restarante
restaurante_df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')



# excluindo colunas
restaurante_df=restaurante_df.drop(['tip','smoker','size','time'],axis=1)

# trocando o nome das colunas
restaurante_df.columns=['Conta_Total','Sex','Dia']

# Agrupando as colunas
restaurante_df=restaurante_df.groupby(['Dia','Sex'],as_index=False,sort=False).agg({'Conta_Total':np.sum})

#criando uma grafico de barra
grf_restarante=px.bar(restaurante_df,x='Dia',y='Conta_Total',color='Sex',barmode='group',
                      color_discrete_sequence=["#FC4C99" ,"#055EA9"],text='Sex',
                      title='Contas paga ao dia por F|M')
# grafico de barra na horizontal
grf_restarante2=px.bar(restaurante_df,y='Dia',x='Conta_Total',color='Sex',barmode='group',
                       color_discrete_sequence=["#FC4C99" ,"#055EA9"],text='Sex',orientation='h',
                       title='Contas paga ao dia por F|M')

grf_restarante.show()

grf_restarante2.show()

