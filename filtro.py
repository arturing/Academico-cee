import tabula
import pandas as pd
from pprint import pprint

# Inicializa listas vazias para armazenar números USP
comp = []
autom = []
energ = []
eletro = []
teleco = []

# Separa as tabelas que existem em cada página
tables = tabula.read_pdf("Resultado-TI-2024-2.pdf", pages="all")

# Analisa cada uma das tabelas
for i in range(len(tables)):
    df = pd.DataFrame(tables[i])  # Transforma cada tabela em um dataframe 
    
    if 'Resultado' in df.columns and 'Número USP' in df.columns:  # Certifica-se que ambas as colunas existem
        comp += df[df['Resultado'] == '31223000']['Número USP'].tolist()
        autom += df[df['Resultado'] == '30323150']['Número USP'].tolist()
        energ += df[df['Resultado'] == '30323190']['Número USP'].tolist()
        eletro += df[df['Resultado'] == '30323180']['Número USP'].tolist()
        teleco += df[df['Resultado'] == '30323160']['Número USP'].tolist()

# Imprime os resultados
print("Computação:")
pprint(comp, indent=4)
print("\nAutomação:")
pprint(autom, indent=4)
print("\nEnergia:")
pprint(energ, indent=4)
print("\nEletrônica:")
pprint(eletro, indent=4)
print("\nTelecomunicações:")
pprint(teleco, indent=4)