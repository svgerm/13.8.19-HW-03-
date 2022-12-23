tickets = int(input("Введите количество необходимых билетов: "))
person = 1

price = 0
while person <= tickets:
    age_for_ticket = int(input(f'Укажите для какого возраста приобретается билет № {person} ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        price += 990
        print('Стоимость билета: 990 руб.')
    else:
        price += 1390
        print('Стоимость билета: 1390 руб.')
    person += 1

if tickets > 3:
    sale = price - (price * (100) ** -1 * 10)
    print(f'Сумма к оплате {sale} руб., применена 10%-ая скидка за покупку более 3 билетов единовременно')
else:
    print(f'Сумма к оплате {cash} руб.')