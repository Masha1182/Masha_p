per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите вносимую сумму:'))
deposit = list(per_cent.values())
deposit[0] = round((deposit[0]*money)/100, 2)
deposit[1] = round((deposit[1]*money)/100, 2)
deposit[2] = round((deposit[2]*money)/100, 2)
deposit[3] = round((deposit[3]*money)/100, 2)
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))

      
