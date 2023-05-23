#https://data.world/toscanocombr/mapainvestimentomgbrasil2019 - link para dataset
import plotly.express as px
from pandas import read_csv, DataFrame

df = read_csv(".\DataSets\mapa_investimento_mg_brasil_2019.csv", header=0, delimiter=';')

df =df[df['Municipio'] == 'BELO HORIZONTE']

municipios = df["Municipio"].values
orgaos = df["Orgao"].values
items_de_despesa = df["Item de Despesa"].values
valor_investido = df["Valor Investido"].apply(lambda x: (x.replace(".", "").replace(",", "."))).astype(float).values

df = DataFrame(dict(municipios=municipios, orgaos=orgaos, items_de_despesa=items_de_despesa))
df["all"] = "all"
fig = px.treemap(df,path=[municipios,orgaos,items_de_despesa],values=valor_investido, title="Mapa de Investimento da cidade de Belo Horizonte, Minas Gerais,Brasil (2019)")
fig.show()