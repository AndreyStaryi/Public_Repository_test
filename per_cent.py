per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

values = list(per_cent.values())
print(values)

money = float(input("Введите сумму вклада:"))

deposit = [money/100 * x for x in values]
print(deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))

