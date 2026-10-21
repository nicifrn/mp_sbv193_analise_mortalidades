obitos = int(input('qual o número de obitos?: '))
populacao = int(input('qual o número da população do municipio?: '))

if populacao > 0:
    
    taxa = (obitos / populacao) * 100000
    print(f'taxa de mortalidade: {taxa:.2f} por 100.000 habitantes')
else:
    print('população deve ser maior que 0')