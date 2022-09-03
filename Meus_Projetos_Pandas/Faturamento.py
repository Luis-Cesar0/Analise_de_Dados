import pandas as pd

#acesso os arquivos
vendas_df=pd.read_excel('F:\Repositorio\Projetos_Python\Meus_Projetos_Pandas\Faturamento_arquivo\Vendas.xlsx')
produto_df=pd.read_excel('F:\Repositorio\Projetos_Python\Meus_Projetos_Pandas\Faturamento_arquivo\Produtos.xlsx')

#selecionado as colunas
vendas_df=vendas_df[['cdg vendas','Qtd comprada','cdg Produto']]


#unindo os dois arquivos
vendas_df=vendas_df.merge(produto_df)

#excluindo colunas
vendas_df= vendas_df.drop(vendas_df[['cdg vendas','cdg Produto','Qtd.']],axis=1)

#multiplicando 'valor unitario ' com a 'Qtd comprada'
vendas_df['valor unitario']= vendas_df['Qtd comprada'] * vendas_df['valor unitario']

#trocando o nome das colunas
vendas_df.columns=['QTD Comprada','Produto','Valor total']

#agrupando as colunas pela nome e somando a quantidade vendida
vendas_df=vendas_df.groupby('Produto').sum()



#salvando a planilha excel
vendas_df.to_excel('F:\Repositorio\Projetos_Python\Meus_Projetos_Pandas\Faturamento_arquivo\Total_Vendas.xlsx')







