# https://data.world/kgarrett/covid-19-open-research-dataset - link para dataset
#pesquisas escolares
from pandas import read_csv
import plotly.graph_objs as go
import json

with open('isoCountryNames.json') as user_file:
  parsed_json = json.load(user_file)
  countries = list(parsed_json.values())

dfData = read_csv(".\DataSets\covid_12-04-2020.csv")

dfData = dfData[dfData['date'] == '2020-06-08']
dfData = dfData.query('location.isin(@countries).values')

data = dict (
 type = 'choropleth',
 locations = dfData['location'],
 locationmode='country names',
 colorscale = 'Reds',
 z=dfData['total_deaths'])

map = go.Figure(data=[data])

map.update_layout(
    title={
        'text': "Mortes por COVID-19 no dia 08/06/2020 - Coleção de artigos academicos diversos - 27 no total",
        # 'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

map.show()