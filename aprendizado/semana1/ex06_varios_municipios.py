taxa_maior = -1
municipio_maior = ""

while True:
    nome = input('digite o nome do municipio ou "fim" para encerrar: ')
    
    if nome.lower() == "fim":
        break

obitos = int(input('digite o número de obitos: '))      
habitantes = int(input('digite o número de habitantes: '))

taxa = (obitos / habitantes) * 100000
print(f'a taxa de mortalidade do muinicipio {nome} é: {taxa:.2f}')

if taxa > taxa_maior:
    taxa_maior = taxa
    municipio_maior = nome
    
print(f'o municipio com a maior taxa de mortalidade é {municipio_maior} com a taxa de {taxa_maior:.2f}')