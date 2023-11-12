# Напишите программу, которая будет рандомно генирировать от 2 до 5 объектов класса Human.
# У каждого объекта этого класса рандомным образом должны определяться следующие свойства:
# 1) Пол: Мужчина или Женщина
# 2) Рандомное имя в зависимости от пола:
# М(Lionel McCoy, Charles Cross, John Pitz, Jeffry Young, Johnathan Randall, Edward Townsend, Lewis Pope)
# Ж(Aubrey Gilmore, Avice Reynolds, Theresa Bradford, Shonda Douglas, Karen Sanders, Ruby Rice, Ruth Rice)
# Можно дополнить своими вариантами
# 3) Возраст: от 18 до 100 лет
# 4) Характер: холерик или сангвиник или меланхолик или флегматик
# 5) Место работы: Рабочий или Безработный
# 6) Рандомный капитал от 100$ до 10000$
# 7) Рандомный ежемесячный доход от 1000$ до 5000$, при наличии работы. Если работы нет, то от 100$ до 300$.
# 8) Рандомная дата рождения в формате xx.xx.xxxx(тип Private)
# 9) Рандомная дата смерти в формате xx.xx.xxxx(тип Private)
# 10) Наличие дома: Свой дом или Аренда
# 11) Наличие машины: Есть или нет
# 12) Семейное положение: Свободен или Женат/Замужем в зависимости от пола
# 13) Дата свадьбы, если статус Женат/Замужем присвоен сразу, то рандомная дата
# в формате xx.xx.xxxx(тип Protected) в диапазоне от даты рождения +18 лет до текущего возраста
# Если изначально статус свободен, то значение None
# 14) Ежемесячные расходы 30% от ежемесячного дохода


import random
import copy


class Human:
    current_year = 2023
    count_job = 0

    def __init__(self):
        self.male = random.choice(('мужчина', 'женщина'))
        self.name = random.choice(('Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice',
         'Ruth Rice')) if self.male == 'женщина' else random.choice(('Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend', 'Lewis Pope'))
        self.age = random.randint(18,100)
        self.haracter = random.choice(('халерик', 'сангвиник', 'меланхолик', 'флегматик'))
        self.job = random.choice(('рабочий','безработный'))
        self.capital = random.randint(100,10000)
        if self.job == 'рабочий':
            self.salary = random.randint(1000,5000)
        else:
            self.salary = random.randint(100,300)
        self.__birthday = self.random_date(self.current_year - self.age)
        self.__death = self.random_date(random.randint(self.current_year, self.current_year + 100 - self.age))
        self.house = random.choice(('свой дом','аренда дома'))
        self.car = random.choice(('есть машина','нет машины'))
        self.family = random.choice(('Свободен', 'Женат' if self.male == 'мужчина' else 'Свободна', 'Замужем'))
        if self.family in ('Женат', 'Замужем'):
            self.weddingdate = self.random_date(random.randint(int(self.__birthday[-4:])+18, int(self.__birthday[-4:])+ self.age))
        else:
            self.weddingdate = None
        self.spending = self.salary*0.3

    def random_date(self, year):
        mounth = random.randint(1, 12)
        dict_mounth = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30,
                       2: 29 if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0 else 28}
        day = random.randint(1, dict_mounth[mounth])
        return f'{day}.{mounth}.{year}'

    def info(self):
        print(f"male: {self.male}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Haracter: {self.haracter}")
        print(f"Job: {self.job}")
        print(f"Capital:{self.capital}")
        print(f"Salary:{self.salary}")
        print(f"Birthday: {self.__birthday}")
        print(f"Death date: {self.__death}")
        print(f"House: {self.house}")
        print(f"Car: {self.car}")
        print(f"Marage: {self.family}")
        print(f"Wedding date: {self.weddingdate}")
        print(f"Spending of money: {self.spending}")

    def life(self):
        self.age += 1
        self.current_year += 1
        if random.randint(1, 30) == 1:
            self.__death = self.random_date(self.current_year)
            # list_death.append(list.pop(list.index(self)))

    def jobs(self):
        dict_character = {'халерик':{'безработный': 2, 'рабочий': 7},
                        'сангвиник':{'безработный': 3, 'рабочий': 10},
                        'меланхолик':{'безработный': 7, 'рабочий': 6},
                        'флегматик':{'безработный': 5, 'рабочий': 20}}
        job = self.job
        if self.job == 'безработный':
            self.job = 'рабочий' if random.randint(1, dict_character[self.haracter][self.job]) == 1 else 'безработный'
        else:
            self.job = 'безработный' if random.randint(1, dict_character[self.haracter][self.job]) == 1 else 'рабочий'
        if job != self.job and self.job == 'рабочий':
            self.count_job += 1
            print('Сменил работу')

list = [Human() for x in range(random.randint(2,5))]
new_list = copy.deepcopy(list)
list_death = []

while len(list) != 0:
    for x in list:
        while x.current_year < int(x._Human__death[-4:]):
            x.life()
        else:
            list_death.append(list.pop(list.index(x)))
        break


while True:
    print('Информацию о ком вы хотите получить?')
    for x in list_death:
        print(f'{list_death.index(x)} - {x.name}')
    choice = int(input('Введите: '))

    print(new_list[choice].info())
    print()
    print(list_death[choice].info())