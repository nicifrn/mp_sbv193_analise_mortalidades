anos = [2020, 2021, 2022, 2023, 2024]
obitos = [383, 362, 490, 429, 354]

total = 0
obito_maior =[0]
ano_maior = anos[0]  
acima_400 = 0  

for i in range(len(anos)):
    total += obitos[i]
    
    if obitos[i] > obito_maior[0]:
        obito_maior[0] = obitos[i]
        ano_maior = anos[i]
        
    if obitos[i] > 400:
        acima_400 += 1

print(f'total de obitos(2020-2024): {total}')
print(f'ano com mais obitos: {ano_maior}')
print(f'numero de anos com obitos acima de 400: {acima_400}')