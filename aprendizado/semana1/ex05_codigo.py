ibge_code = input("Digite o código de 7 dígitos: ")

if len(ibge_code) != 7:
    print('Codigo invalido.') 
else:
    six = (ibge_code)[0:6]
    print(f'Os seis primeiros dígitos do código são:{six}')
    seven = (ibge_code)[6]
    print(f'O último dígito do código é: {seven}')