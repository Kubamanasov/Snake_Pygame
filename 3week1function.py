#  ФУНКЦИИ

# def name_of_function()
#     some_code
#     return variable
# name_of_function()

# def fuction():
#     print('функ работат')
#     return 'kuba'

# print(fuction())

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2
# substract() -> так выводит то что + овали в принте

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2
# print(substract()) -> так выводит то что мы прописали в return е

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2
# # substract() -> так выводит то что + овали в принте

# variable = substract() #-> к функции можно ввеестив перемнный
# print(variable)

# list_=[1, 2, 3, 4, 5, substract()]
# print(list_) -> можно внести  их в словари таким образом

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2 

# def fuction():   -> так можно вызвать внутри одной функции другую функцию
#     print('i am calling substract function')
#     print(substract()) -> что зараболтала return обизательно надо его в принт впихать
# print(fuction())


# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2 

# def fuction():  # -> так можно вызвать внутри одной функции другую функцию
#     print('i am calling substract function')
#     variable = substract()
#     return variable
# print(fuction())

# def multiply(a, b):
#     return a * b
# num1 = 70
# num2 = 10
# print(multiply(num1, num2))

# def welcome(name, lat_name):
#     return f'welcome, {name} {lat_name}'
# name = input()
# lat_name=input()
# print(welcome(name, lat_name))

# def get_word(word):
#     list_letters =  list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels=['a', 'o', 'y',  'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     result = ''.join(list_vowels)
#     return result

# my_word=input('enter the word: ')
# print(get_vowels(get_word(my_word)))

# def info(name='kuba', age=21):
#     return f'{name} is {age} years old.'
# print(info()) -> если ничего не ввести внутрь то оно выводит нам дефелтные значение None  или ж то что мы ввели в начале как шас

# def info(name='kuba', age=21):
#     return f'{name} is {age} years old.'
# print(info(age=21, name='Kuba')) -> а если введем значение то дефелтные значаение котрое мы ввели в начале они не сработают а сработают то что мы тут внутри ввели


# def info(name, age):
#     return f'{name} is {age} years old.'
# print(info('Kuba', age = 2224))# ->  сначало идет позиционнный а потом именнованный если орно есть 


# def test_func(n1=2, n2=9):
#     return n1 + n2

# print(test_func())

# def creat_profile(name, age, image='vlakvalk'):
#     return name, age, image

# print(creat_profile('Kuba', 21)) -> так мы не указали внутри скобки только image и оно нам вывела который по дефолту стоит 

    # *args **kwargs  -> являются дополлнительными операторами которые не обьезательно ввести в скобке
#   тут args обазначается с одним * ом а kwargs с двумя ** оми ...  и тут главное ввести перед 
#   словам звезочки а название args и kwargs можно заменять на любые лругие слова

# def func(required, *args, **kwargs):
#     print(required) -> kuba

#     if args:
#         print(args) -> ('manas', 'mk')

#     if kwargs:
#         print(kwargs) -> {'name': 'voker', 'age': 21}

# func('kuba', 'manas', 'mk', name='voker', age=21)


# def many(*args, **kwargs):
#     print(args) -> приходит сюда только позиционнные аргументы
#     print(kwargs) -> а сюда приходит только  именнованные аргументы
# many(1, 2, 3, name='boss', job='gamer')




    #    РАЗБОР ТАСКОВ

"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def multiply(a, b):
#     return a + b
# num1 = 70
# num2 = 10
# print(multiply(num1, num2))

# def x(a,s):
#     return a+s
# q=2
# w=3
# print(x(q, w))


"""
2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки.
"""
# def get_word(word):
#     list_letters=len(word)
#     return list_letters
# print(get_word('kuba'))
"""
3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# """
# def x(a='kuba', s=2):
#     return type(a), type(s)
# print(x())

# def info(name, age):
#     return f'{name} is {age} years old.'
# print(info('Kuba', age = 2224))# ->  сначало идет позиционнный а потом именнованный если орно есть 

"""
4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def a(num1, num2):
#     return num1 / num2
# print(a(10, 5))
"""
5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
# """
# def x(**kwargs):
    
#     if kwargs:
#         print(kwargs)

# x(name='kuba', last_name='manasov')

"""
6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
"""
# def x (a):
#     if a % 2 ==0:
#         print("It's odd number")
#     else:
#         print("It's even number")
# print(x(5))
"""
7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
"""
# def x(a):
#     if a == a[::-1]:
#         print(True)
#     else:
#         print(False)

# x('kok')
# x('kuba')
"""
8) Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
"""
# def x(a, b):
#     return max(a, b)

# print(x(input('введите первое: '), input('введите второе: ')))
"""
9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def x(*num):
#     a=1
#     for i in num:
#         a *= i
#     return a
# print(x(1, 2, 3, 4))


 
# 10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр. 
# 10 ----- для исправлени в таске

# def a(num):
#     s = 0
#     for d in str(num):
#         s += int(d)

#     return s

# z = a(125)
# print(z)


# def a(num):
#     return sum([int(d) for d in str(num)])

# z = a(1252)
# print(z)


# def a(num):
#     return sum([int(d) for d in str(num)])

# z = a(1252)
# print(z)
#  







    #    РАЗБОР  С АДИЛЕТОМ

# ФУНКЦИИ  - вазможность переиспользование кода без переписки


#  обьявление функции
# function definition
# def func(0):
#     тело функции

#вызов функции
#function call
# func()


# num1=15
# num2=13
# num3=5
# num4=6
# num5=10

# fact1=1
# for i in a range(1, num1 + 1):
#     fact *= i
# print(fact) -> так для каждого номера придется код писат что бы найти фактериалы

# numbers=[num1, num2, num3, num4, num5]
# for num in numbers:
#     fact=1
#     for i in range(1, num+1):
#         fact *= i
#     print(fact) -> а тут в листе может быть очень много значение поэтому это тоже не гибкий вариант


# def factorial(number):
#     fact = 1 
#     for i in range(1, number +1):
#         fact *= i
#     return fact

# res = factorial

#                             Аннотация типов
# def factoorial(num: int) -> int:
#     тело функции

#  ........................документация функции 
# def factorial(number):
#     '''оно Принимает число и возвращает его факториал'''
#     тело функции
# def func():
#     pass
# def func1(x):
#     pass

# def func2(x, y, z)


#  ПАРАМЕТРЫ ьыввают не обязательные и по умолчанию (не обьязательно)

# def func(x, y=1):
#     return x+y

# print(func(3))
# ////////////////////////////////

# def current_time():
#     import datetime
#     return datetime.datetime.now()


# def chemical_reaction():
#     if temperature > 105:
#         alert()

# def func(x, y=1):
#     ...

# func(2) -> x=2, y=1
# func(2, 5) -> x=2, y=5
# func(2, y-=2) ->

# ///ПРАВЛИА......  --- в при вызове функции сночала должны передаватся позиционные аргументы и только потом именованные
# func(x=2, 5) -> ошибка
# func(2, x=5) -> ошибка мы тут передаем 2 значеие в 'x'


# def chemical_reaction(temp, pressure):  -> параметры
#     if temp > 100:
#         ...

# chemical_reaction(1005, 2.5)   -> аргументы    ... это значение для параметра


# def func(x: int, y: int):  ->  int:  -> тут эти считаются как коментарии
#     return x+y

# func('1', '2') -> '12'
# func([1, 2, 3], [4, 5, 6]) -> 1, 2, 3, 4, 5, 6

# num1='1'
# num2=2

# когда прилетают непонятно какого классса просто переделаем его в нам нужный тип
# num1 = int(num1)
# func(num1, num2)

#           *args, **kwargs

# list_=[1, 2, 3, 4]
# a, b, c, d = list_
# a -> 1
# b -> 2
# c -> 3
# d -> 4


# list_=[1, 2, 3, 4, 5, 6]
# a, b, *c = list_
# a -> 1
# b -> 2
# c -> [3, 4, 5, 6]

# new_list=[c, 7, 8, 9]
# new_list -> [[3, 4, 5, 6], 7, 8, 9]
# new_list1 = [*c, 7, 8, 9]  -----------> "*" может использоваться для того что бы их собрать в список и внитри списка наоборот как тут
# new_list1 -> [3, 4, 5, 6, 7, 8, 9]


# def func(x, y):
#     return x + y
# func([1, 2]) -> ошибка
# func(*[1, 2]) -> без ошибок   "*" используется для раскрытии скобок тоже

# dict1={'x': 1, 'y': 2}
# func(**dict1)   -> а словари так используем


# def noti_users(*emails):
#     for mail in emails:
#         send_massage(email)


# noti_users('1@gamill.com', '2@gamill.com', '3@gamill.com')  -> так мы можем рассылать многим емейлам


#         pass - каманда указывающий ничего не делать  - можно почти в любом месте его использоваьт что бы код наш работал. то есть это говорит что что я вместо pass потом когда додумаю использую вс=место него что то а пока пусть кода работаетбез ощибок

# func ():
#     pass


# def avg(*nums):
#     return sum(nums) / len(nums)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# print(avg(2, 3, 4, 5, 6, 7, 8, 9)) #-> варик 1

# print(avg(*numbers)) #-> варик 2


# def func(a, b, c=1, *args, **kwargs):
#     pass

# func(1, 2, 3, 4, 5, 6)
# a->1
# b->2
# c->3
# *args->(4, 5, 6)

# func(a=1, b=2, c=3, d=4, e=5, f=6)
# a->1
# b->2
# c->3
# **kwargs -> {'d': 4, 'e': 5, 'f': 6}

# def crear_user(email, password, **extra_fields):
#     user=_creat_user(emeil, password)
#     for key, value in extra_fields.items():
#         setattr(user, key, value)

# crear_user(emeil='test@mail.ru', password='qwerty', first_name='ivan', last_name='ivanov')




                            # a='this is a test string'

                            # a.find('h') -> 1
                            # a.find('h', start5, end=10)
                            # def find(sub, start=0, end=None):
                            #     if start

# a={1, 2, 3, 4, 5}
# a.update({1, 2, 3}, {4, 5, 6, 7})

# def update(*s):
#     ....