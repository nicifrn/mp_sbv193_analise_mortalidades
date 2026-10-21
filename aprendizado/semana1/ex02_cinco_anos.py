obitos_2020 = int(input('qual o número de obitos em 2020?:'))
obitos_2021 = int(input('qual o número de obitos em 2021?:'))
obitos_2022 = int(input('qual o número de obitos em 2022?:'))
obitos_2023 = int(input('qual o número de obitos em 2023?:'))
obitos_2024 = int(input('qual o número de obitos em 2024?:'))

total = obitos_2020 + obitos_2021 + obitos_2022 + obitos_2023 + obitos_2024
print(f'total de obitos(2020-2024): {total}')
media = total / 5
print(f'média de obitos(2020-2024): {media:.2f}')