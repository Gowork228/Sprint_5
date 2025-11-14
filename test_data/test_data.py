import random

class MyTestData:
    USER_NAME = 'Анна Кульпо'
    LOGIN = 'hanna_kulpo_34_111@mail.ru'
    PASSWORD = 'aa34AA'

class RandomTestData:
    USER_NAME = 'Лео Леович'
    LOGIN = f'leoleo{random.randint(100,999)}@yandex.ru'
    PASSWORD = f'lll{random.randint(100,999)}LLL'