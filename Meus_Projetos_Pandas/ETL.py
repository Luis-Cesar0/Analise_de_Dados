import pandas as pd
import sqlalchemy

#criando uma conição com o banco MySQL
myBanco_con=sqlalchemy.create_engine('mysql+pymysql://<username>:<password>@<host>/<notas_alunos>[?<options>]')

#acessando a tabela do banco de dados
mynotas_df=pd.read_sql(sql='SELECT * FROM notas',con=myBanco_con,)

#excluindo colunas
mynotas_df=mynotas_df.drop(['idAlunos','altura','peso'],axis=1)

#criando uma coneção com outro banco de daos
serve_con=sqlalchemy.create_engine('mssql+pyodbc://scott:tiger@myhost:port/notas_alunos?driver=ODBC+Driver+17+for+SQL+Server')



#caculo da chunksize
chu= 2097 // len(mynotas_df.columns)
if chu > 1000:
 chu= 1000
else:
 chu = chu

#Enviando para outro banco de dados
serv_chegada=mynotas_df.to_sql(name='notas',con=serve_con,index=False,if_exists='replace',chunksize=chu)


