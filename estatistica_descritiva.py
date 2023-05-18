#https://data.world/toscanocombr/mapainvestimentomgbrasil2019 - link para dataset
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

fields = ["orgao","valor_empenhado","valor_liquidado","valor_pago"]

df = read_csv(".\DataSets\mapa_investimento_mg_brasil_2019.csv",
              header=0,
              names=fields,
              delimiter=';').query('Municipio' == 'BELO HORIZONTE')


# 3. musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
# 4. indice = np.arange(len(musicas))
# 5. acessos = [1068254,866216,849895,763652,758198]

# plt.bar(indice, acessos)
# plt.xticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Mapa de investimento do governo de minas gerais - Brasil - 2019')


# pos = list(range(len(df['valor_empenhado'])))
# width = 0.25

# fig, ax = plt.subplots(figsize=(10,5))

# plt.bar(pos, df['valor_empenhado'], width, alpha=0.5, color='#EE3224')
# plt.bar([p + width for p in pos], df['valor_liquidado'], width, alpha=0.5, color='#F78F1E')
# plt.bar([p + width*2 for p in pos], df['valor_pago'], width, alpha=0.5, color='#FFC222')

# Setting the y axis label
# ax.set_ylabel('Valore gastos (Em R$)')

# # Setting the chart's title
# ax.set_title('Despesas Estaduais MG Brasil - 2019')

# # Setting the position of the x ticks
# # ax.set_xticks([p + 1.5 * width for p in pos])

# # Setting the labels for the x ticks
# ax.set_xticklabels(map(df['orgao'])), rotation=90)

# # Setting the x-axis and y-axis limits
# # plt.xlim(min(pos)-width, max(pos)+width*4)
# # plt.ylim([0, max(df['valor_empenhado'] + df['valor_liquidado'] + df['valor_pago'])] )

# # Adding the legend and showing the plot
# plt.legend(['valor_empenhado', 'valor_liquidado', 'valor_pago'], loc='upper left')
# plt.grid()
# plt.show()
# # groups = df[["valor_empenhado","valor_liquidado","valor_pago"]].values
# # group_labels = df["orgao"]

# # df = DataFrame(groups, index=group_labels).T

# # concat(
# #     [df.mean().rename('average'), df.min().rename('min'), 
# #      df.max().rename('max')],
# #     axis=1).plot.bar()

# # musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
# # 4. indice = np.arange(len(musicas))
# # 5. acessos = [1068254,866216,849895,763652,758198]
# # 6. plt.bar(indice, acessos)
# # 7. plt.xticks(indice, musicas)
# # 8. plt.ylabel('Acessos')
# # 9. plt.title('Ranking do Spotify 31.dez.2019')
# # 10. plt.show()

