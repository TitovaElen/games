
# Казино. Всё начинается со стартового меню, с вопросом: хотите ли сыграть? Y/N - ДА/НЕТ.
# Дальше реализуем пополнение баланса пользователя, он сам должен ввести сумму, которую хочет
# использовать для игры.
# После чего компьютер генерирует числа от 1 до 10 и один из цветов, красный или черный.
# Пользователю дается столько попыток, сколько он купил, чтобы угадать номер и цвет.
# Выводить соответствующие сообщения о том, угадал ли пользователь что-то и сколько
# попыток у него еще осталось. Например: "Вы угадали только цвет, у вас осталось 4 попытки".
# В случае если пользователь уже отгадал число или цвет, то больше не просить его снова вводить
# то, что он уже отгадал.
# купить еще или завершить игру, если он покупает, то игра продолжается, если он не покупает или,
# если у него денег меньше, чем стоимость одной жизни, то вывести на экран сообщение о проигрыше
# и правильную комбинацию.
# В случае победы начислять на баланс игрока сумму равную стоимости 7 жизней,
# после чего запрашивать хочет ли игрок продолжить игру, и при утвердительном ответе
# сохранять за ним уже имеющееся кол-во жизней, но при этом число и цвет должны генерироваться
# новые, а при отрицательном ответе переводить имеющиеся у игрока жизни в баланс и выводить на
# экран баланс игрока, т.е. его выйгрыш, после чего баланс должен сбрасываться и программа должна
# снова выводить на экран то, что было в начале "хотите ли сыграть? Y/N - ДА/НЕТ", а дальше всё по
# тому же сценарию, что и с первым игроком, тем самым давая возможность поиграть новому игроку без
# перезапуска программы.


import random

start = input('Хотите ли вы сыграть в казино: да или нет?: ')
if start == 'да':
    balance = int(input('Введите сумму депозита: '))
    price_try = 5
    while True:
        number_try = int(input(f'Стоимость одной попытки - {price_try} фишек. Введите сколько купить: '))
        if balance >= price_try * number_try:
            balance -= price_try * number_try

            num = random.randint(1, 10)
            color = random.randint(1, 2)
            while number_try:
                num_player = int(input('Введите число от 1 до 10: '))
                color_player = int(input('Введите число от 1 до 2(1 - красный, 2 - черный): '))

                if num_player in range(1, 11) or color_player in range(1, 3):
                    number_try -= 1
                else:
                    print('Error: введите данные некорректно')
                    continue

                if num == num_player and color == color_player:
                    balance += price_try * 7
                    print(f'Вы выиграли. У вас {balance} фишек, осталось {number_try} попыток.')
                    choice = int(input('1 - продолжить игру\n2 - забрать выигрыш\nВведите число: '))
                    if choice == 1:
                        num = random.randint(1, 10)
                        color = random.randint(1, 2)
                        continue
                    elif choice == 2:
                        balance += number_try * price_try
                        print(f'Ваш выигрыш {balance}.')
                        break
                elif num == num_player:
                    print(f'Угадали число, но не угадали цвет. У вас осталось {number_try} попыток.')
                elif color == color_player:
                    print(f'Не угадали число, но угадали цвет. У вас осталось {number_try} попыток.')

                if number_try == 0:
                    print('У вас закончились попытки.')
                    if balance >= price_try:
                        choice = int(input('1 - купить попытки\n2 - завершить\nВведите число: '))
                        if choice == 1:
                            while True:
                                number_try = int(
                                    input(f'Стоимость одной попытки - {price_try} фишек. Введите сколько купить: '))
                                if balance >= price_try * number_try:
                                    balance -= price_try * number_try
                                    break
                                else:
                                    print(f'Не хватает денег на {number_try}. Но хватает на {int(balance / price_try)}')
                                    continue
                        elif choice == 2:
                            break
                    else:
                        break
        elif balance < price_try:
            print('Денег не хватает даже на одну попыткую. Пополните баланс.')
            balance += int(input(f'У вас на счету {balance}. Сколько добавить?: '))
            continue
        else:
            print(f'Не хватает денег на {number_try}. Но хватает на {int(balance / price_try)}')
            choice = int(input('1 - пополнить баланс\n2 - покупка попыток\nВведите число: '))
            if choice == 1:
                balance += int(input(f'У вас на счету {balance}. Сколько добавить?: '))
                continue
            elif choice == 2:
                continue
        print(f'Вы проиграли. Было загадано число {num} и цвет {color}')
        print(f'Ваш баланс {balance}. Заберите деньги.')
        break
