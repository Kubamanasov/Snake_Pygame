"""
built-ins - встроенная пространства имен
global - глобальная
enclosed - локальная пространства имен
local - 
"""

# this_var_is_visible='you can see inside and outside the function'

# def var_visibilite():
#     this_var_is_not_visible='You can see me only insisde the function'
#     print(this_var_is_not_visible)

# print(this_var_is_visible)
# var_visibilite()

# from урок4 import variable -> так можно импортировать переменные с других файлов 
# print(variable) 


#          built-ins
# print(dir(__builtins__)) -> ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 
# 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
#  'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 
#  'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 
#  'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
#  'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError',
#   'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
#    'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
#    'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
#     'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 
#     'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__',
#      '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii',
#       'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#        'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
#        'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
#         'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord',
#          'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
#          'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']



    # name = 'Kuba'
    # name = 'Boss'
    # print(name)

# word = "I'am global"  - глобал
# def func_a():
#     word = "I'am local" - локал
#     print(word)

# func_a()
# print(word)


# word = "I'am global"  -> глобал
# def outer():
#     word="I'am enclosed" -> замкнутый пространства имен. потомучто оно стоит между глобалом и локалом
#     print(word)

#     def inner():
#         word="I'am local" -> локал
#         print(word)

#     inner()
# outer()
# print(word)


# word = "I'am global" # -> глобал
# def outer():
#     word="I'am enclosed"# -> замкнутый пространства имен. потомучто оно стоит между глобалом и локалом
#     print(word)
#     inner()

# def inner():
#     word="I'am local" #-> локал
#     print(word)
 
# outer()
# print(word)


            # globals(), locals()

# name = 'kuba'
# name = 'Manasov'
# print(globals())


# def func(a):
#     name='Boss'
#     name='kuba'
#     print(locals())

# func(a='mk')

# def info(name, age):
#     name='Kuba'
#     age=21    -> тут срабатывает последним поэтому принт нам вывводит это значаение. потому что в переменну перезаписовается новые значение
#     print(locals())  -> {'name': 'Kuba', 'age': 21}

# info(name='mk', age=25) -> срабатывает первее

# print(globals()) 
# print(locals()) -> если в локалное простронства ничего не задавать оно ссылается в пространства глоабал. и поэтому в данным примере глобал и локал принты выводит нам одинаковый результат

# def outer():
#     name = 'kuba'

#     def inner():
#         nonlocal name -> такой же как локал и глобал но тут оно ищет только в замкнутом пространстве. тут у нас также перезаписовается то то присвоено последним
#         name='boss'
         
#     inner()
#     print(name)

# outer()


# ////////////// ТАСКИ РАЗБОР ///////////////////////

"""
1) У Ирины футболки 2 цветов. Ирина одевает красную футболку в чётные числа месяца, 
а синюю в нечётные. Напишите программу, которая по введённому числу месяца определяет
 какую футболку нужно одеть Ирине сегодня.
"""
# def x(a):
#     if a % 2 == 0:
#         print('одевай красную футболку')
#     else:
#         print('одевай синюю футболку')

# x(int(input('введите сегодняшний день месяца: ')))

# def x(a):
#     if a % 2 == 0:
#         print('одевай красную футболку\nможешь узнать что завтра одевать ведя завтрашний день: ')
#     def x(a):
#         if a % 2 == 1:
#             print('одевай синюю футболку ')
#     x(int(input('еще раз введите день месяца: ')))

# x(int(input('введите сегодняшний день месяца: ')))

"""
2) Пользователь должен ввести 2 целых числа, Вам необходимо проверить делится ли первое число на второе. Вывести результат, а также остаток от деления (если есть).
"""



# def x(a, s):
#     if a / s:
#         print(f'\tрезультат: {a/s}')
#         print(f'остаток от деление: {a%s}')
# x(int(input('введите первое число: ')), int(input('введите второе число: ')))
"""
3) Вам дано три числа, используйте условные операторы и выведите на экран наибольшое из них.
"""
# def x(a, s, d):
#     return max(a, s, d)

# print(x(int(input('введите первое число: ')), int(input('введите второе число: ')), int(input('введите третье число: '))))

# def x(a, s, d):
#     if a>s and a>d:
#         print(a)
#     elif s>a and s>d:
#         print(s)
#     elif d>a and d>s:
#         print(d)
# x(a=12, s=6, d=33)
# print(x(int(input('введите первое число: ')), int(input('введите второе число: ')), int(input('введите третье число: '))))
"""
4) Вам дан список из чисел. Напишите функцию, которая вернёт новый список из квадратов этих чисел.
"""

# def x(*a):
#     s=[v**2 for v in a]
#     return s
        
# print(x(*[1, 2, 3, 4, 5]))
    
"""
5) Вам дан список из целых чисел. Напишите функцию,
в которой Вам необходимо найти факториал каждого из чисел и записать в новый список.
"""
# z=[1, 2, 3, 4, 5, 6]
# def x(a):
#     fact = 1 
#     for i in range(1, a+1):
#         fact *= i
#     return fact

# print(x(z[index]))

# z=[1, 2, 3, 4, 5, 6]
# def x(a):
#     res=(fact *= fact for fact in range(1, a+1))
#     return res 
# print(x([2]))

# a=list(range(1, 11))
# def factorial(a):
#     fact = 1
#     new_a = []
#     for i in a[:]:
#         fact *= i
#         new_a.append(fact)
#     return new_a
# print(factorial(a))

# def factorial(a=list(range(1, 11))):
#     fact =1
#     new=[]
#     for i in a[:]:
#         fact *= i
#         new.append(fact)
#     return new
# print(factorial(a))


"""
6) Мурат с друзьями на выходных решил собратся и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24, Эржану - 21, Чынгызу - 24, Алтынай - 17, Асеме - 16.
Напишите программу которая определяет кого пустить в ночной клуб, а кого нет.
"""
# def x(**kwargs):
#     for key, value in kwargs.items():
#         if value >= 17:
#             print(f'вам разрешено: {key}')
#         else:
#             print(f'вам запрещено: {key}')
#     return
# leute={'murat': 24, 'erjan': 21, 'chyngyz': 24, 'altynai': 17, 'asema': 16}
# x(**leute)
"""
7) Вам дан список из нескольких имён в нижнем регистре.
 Напишите функцию которая записывает начинает первую букву имени в верхнем регистре
  и сохраните в новом списке.
"""
# def x(*args):
#     new=[]
#     for i in args:
#         s=i.capitalize()
#         new.append(s)
#     return new
    
# print(x('kuba', 'manas', 'boss'))

"""
8) Напишите функцию, которая принимает строку и выводит количество гласных,
 согласных букв и остальных символов. Используйте только кириллические символы
"""
# vowels = ['a', 'ю' итд]
# isalpha() and letter in vowels

# glas=['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# def x(a):
#     for i in a:
#         if i.isalpha():
#             if i == glas:
#                 print(len(glas in i))
#         else:
#             pass

# x('куба')

# def x(word):
#     a=[]
#     s=[]
#     vowels = 0
#     consonants = 0
#     for letter in word:
#         if letter.isalpha():
#             if letter.lower() in 'ауоыиэяюёе':
#                 vowels += 1
#                 a.append(vowels)
#             else:
#                 consonants += 1
#                 s.append(consonants)
#     print(f'гласные: {len(a)}')            
#     print(f'согласные: {len(s)}')
#     return 
# x('кубанычбек')

def x(word):
    a=[]
    s=[]
    vowels = 0
    consonants = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'ауоыиэяюёе':
                vowels += 1
                a.append(vowels)
            else:
                consonants += 1
                s.append(consonants)
    print(f'гласные: {len(a)}')            
    print(f'согласные: {len(s)}')
    return 
x('кубанычбек')
"""
9) Создайте пустой список. Напишите программу которая должна записывать
 в Ваш список числа от 0 до 10 включительно.
"""
# def x(*s):
#     a=[]
#     for i in range(-1, 10):
#         i += 1
#         a.append(i)
#     print(a)  
#     return
# x()

# res = []
# def res2(res):
#     for i in range(0, 11):
#         res.append(i)

# res2(res)
# print(res)
"""
10) Вам дан список целых чисел. Напишите программу которая выводит все элементы, которые меньше 7. 
"""
# q=[]
# def x(*a):
#     for i in a:
#         if i>7:
#             i += i
#             q.append(i)
#             print(q)

# x(1, 3, 5)


# def x(*a):
#     num = [num for num in numbers if int(num) < 7]
#     print(num)
#     return

# numbers = [4, 5, 8, 9, 7, 1, 3, 6]
# x(*numbers)




# ////////////////////////////  РАЗБОР С АДИЛЕТОМ   //////////////////////////////////////////////////////

# ПРОСТРАНСТВА ИМЕН
# namespace
#              .......local ........   -
# a=3 #-> глобальная переменная
# def func(x):
#     print(locals()) -> выводит список локальных переменных. locals - это встроенная Функция
#     b=2  #-> локальная
#     return x+b+a

# func(2)

# if a>2:
#     b=2

# print(b)

# list1=[1, 2, 3, 4, 5]
# for i in list1:
#     y = i
# print(y)
# .....................enclosed(nonlocal)...............

# x=1 #-> глобал
# def func1():
#     a=1 #-> нелокальная переменная
#     def func2():
#         y=10 #-> локальная переменная
#         print('hello world!')
#     return func2



# ....................  globals   ...........
# a=2
# def func():
#     print('hello world')

# class A:
#     pass

# def func2():
#     print(a+10)
#     func1():
#     obj = A
# ..................    built-in   ...............

            # print()
            # len()
            # import os
            # import math ->итд

# global ->  оператор для образение к глобальным переменным
# nonlocal -> оператор для обращение к переменным обьемлющей функции. (обьемлющей функции) -> функция которе держит в себе еще функции

# a=1
# def func(x):
#     global a   -> внутри функции обращаемся к глобольному переменной
#     if x>10:
#         a=2
#     else:
#         a=3

#     return a
# func(1)
# print(a)

# a=1
# def func1():
#     a=10
#     b=5
#     def func2():
#         nonlocal a        -> с при помощью nonlocal обоащаемя к замкнутому пространству переменных итд
#         if b>3:
#             a=21
#         else:
#             a=11  
#             print(a)      
#     func2()
#     print(a)

# func1()
# print(a)


# def func1():
#     a=1
#     def func2():
#         nonlocal a
#         b=10
#         def func3():
#             nonlocal  a
#             print(a)
#         func3()
#     func2()
# func1()







