import pandas as pd
import sqlalchemy

#conequeção com MySQL
origem_con=sqlalchemy.create_engine('mysql+pymysql://<username>:<password>@<host>/<curso_etl_work>[?<options>]')

#armazenado as tabelas em variaveis
fatos_pedi=pd.read_sql(sql='SELECT * FROM fato_pedidos',con=origem_con)
dim_loja=pd.read_sql(sql='SELECT * FROM dim_lojas',con=origem_con)
dim_pro=pd.read_sql(sql='SELECT * FROM dim_produtos',con=origem_con)

#juntando as tabelas
join_tab=pd.merge(left=fatos_pedi,right=dim_pro,how='left',left_on='produto',right_on='id')
join_tab=pd.merge(left=join_tab,right=dim_loja,how='left',left_on='loja',right_on='id')

#excluindo colunas
join_tab=join_tab.drop(columns=['id_x','id_y','id','produto_x','loja'])

#organizando as colunas
join_tab=join_tab[['produto_y','valor','data','estado','cidade','logradouro']]

#renomeando as colunas
join_tab.rename(columns={'produto_y':'Produto','valor':'Preço','data':'Data','estado':'Estado','cidade':'Cidade','logradouro':'Endereço'},inplace=True)

#conequeção com sql serve
chegada_con= sqlalchemy.create_engine('mssql+pyodbc://scott:tiger@myhost:port/curso_ETL?driver=ODBC+Driver+17+for+SQL+Server')

#calculo do chunksize
chu= 2097 // len(join_tab.columns)

#limitador caso o numero de chunksize seja grande
if chu > 1000:
 chu= 1000
else:
 chu = chu

#mandado a tabela para o SQL Serve
join_tab.to_sql(name='pedidos',con=chegada_con,if_exists='replace',index=False,chunksize=chu)



