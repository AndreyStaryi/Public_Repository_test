clients = int(input("Введите количество посетителей: "))
C = clients

list_ages = [int(x) for x in input("Введите возраст посетителей, в соответствии с введённым количеством посетителей: ").split()]
A = len(list_ages)
count_1 = len([x for x in list_ages if x < 18])
P_1 = count_1*0
count_2 = len([x for x in list_ages if 18 <= x < 25])
P_2 = count_2*990
count_3 = len([x for x in list_ages if x >= 25])
P_3 = count_3*1390
P = P_1+P_2+P_3
if A != C:
    print("Количество введённых возрастов не соответствует количеству посетителей.")
else:
    if clients > 3:
        price_discount = P-P//10
        print("Общая стоимость билетов с учётом скидки:", price_discount, "руб.")
    else:
        print("Общая стоимость билетов:", P, "руб.")
