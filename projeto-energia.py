import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
data = pd.read_csv('.\dataset-projeto\global-data-on-sustainable-energy (1).csv')

# Filtrar os países de interesse
paises = ["Madagascar", "Egypt", "Pakistan", "China", "Papua New Guine", "Australia", "Haiti", "Brazil", "Greece", "Germany"]
dados_filtrados = data[data['Entity'].isin(paises)]

# Calcular o espaço de variação entre o acesso à energia dos países
espaco_var = dados_filtrados.groupby('Entity')['Access to electricity (% of population)'].max() - dados_filtrados.groupby('Entity')['Access to electricity (% of population)'].min()
print("Espaço de variação entre o acesso à energia dos países:")
print(espaco_var)

# Calcular a média dos percentuais de pessoas que possuem acesso à energia elétrica nos anos 2000 - 2020
media_acesso_nrg = dados_filtrados.groupby('Entity')['Access to electricity (% of population)'].mean()
print("\nMédia dos percentuais de pessoas com acesso à energia elétrica (2000-2020):")
print(media_acesso_nrg)

# Calcular a capacidade de geração de energia renovável per capita
dados_filtrados['Renewable-electricity-generating-capacity-per-capita'] = pd.to_numeric(dados_filtrados['Renewable-electricity-generating-capacity-per-capita'], errors='coerce')
capacidade_per_capita = dados_filtrados.groupby('Entity')['Renewable-electricity-generating-capacity-per-capita'].max()

print("\nCapacidade de geração de energia renovável per capita:")
print(capacidade_per_capita)

# Calcular a quantidade de eletricidade gerada a partir de combustíveis fósseis em TWh (2000-2020)
dados_filtrados['Electricity from fossil fuels (TWh)'] = pd.to_numeric(dados_filtrados['Electricity from fossil fuels (TWh)'], errors='coerce')
geracao_combust_fossil = dados_filtrados.groupby('Entity')['Electricity from fossil fuels (TWh)'].sum()
print("\nQuantidade de eletricidade gerada a partir de combustíveis fósseis (TWh):")
print(geracao_combust_fossil)

# Criar um boxplot comparando cada país
plt.figure(figsize=(12, 8))
boxplot = plt.boxplot([dados_filtrados[dados_filtrados['Entity'] == pais]['Access to electricity (% of population)'] for pais in paises], labels=paises, vert=False, patch_artist=True)

# Aumentar o tamanho da figura
plt.title('Comparação do Acesso à Energia Elétrica por País (2000-2020)')
plt.xlabel('Percentual de Acesso à Energia Elétrica')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()
