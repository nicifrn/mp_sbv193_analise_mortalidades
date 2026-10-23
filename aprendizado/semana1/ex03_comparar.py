taxa_municipio = float(input('qual a taxa do município?: '))
taxa_estado = float(input('qual a taxa do estado?: '))

if taxa_municipio > taxa_estado:
    print('taxa do município está acima da do estado')

elif taxa_municipio == taxa_estado:
    print('taxa do município está igual à do estado')

else:
    print('taxa do município está abaixo da do estado')