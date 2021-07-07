"""
print()
input()
int()
str()
bool()
list()
dict()
set()
tuple()
frozenset()
len()
sum()
min()
max()
sorted()
"""

     # map(func, iterable object)
                                    # list_str=['1', '2', '3', '4']
                                    # list_int=[]
                                    # for i in list_str:
                                    #     list_int.append(int(i))
                                    # print(list_int)       ------> длинный способ с циклом

                                    # list_str=['1', '2', '3', '4']
                                    # list_int=list(map(int, list_str))
                                    # print(list_int)  ------->быстрый способ с помощью map


# def capital(word: str) -> str:   
#     return word.title()

# list_names=['kuba', 'mk', 'voker']
# new_list=list(map(capital, list_names))
# print(new_list)  -> перевод первых букв в заглавный



# def dollars_to_soms(dollars: int) -> int:
#     return f'{round(dollars * 84.80)} soms'

# dollars = [100, 50, 25, 90, 65]
# soms = list(map(dollars_to_soms, dollars))
# print(soms)  #-> перевод долларов в сом


       # lambda
# print((lambda x: x ** 2) (25))

# square = lambda x: x ** 2
# print(square(25))

# print((lambda x, y, z: x+y+z)(1, 2, 3))  -> необходимо задавать столько аргументов сколько обьявлено в параметрах


# list1=[1, 2, 3]
# list2=[4, 5, 6]
# list3=[7, 8, 4]
# new_list=list(map(lambda x, y, z: x*y*z, list1, list2, list3))
# print(new_list)



# num_list=[1, 2, 3, 4, 5]  ->  с помощью цикла
# numlist2=[]
# for i in num_list:
#     numlist2.append(i*2)
# print(numlist2)

# num_list=[1, 2, 3, 4, 5]   -> с помощью лист компрехеншон
# num_list2=[i*2 for i in num_list]
# print(num_list2)

# num_list=[1, 2, 3, 4, 5]    -> с помощью map+lambda
# num_list2=list(map(lambda i: i*2, num_list))
# print(num_list2)


# /////////// filter ///////////

# names=['kuba', 'voker', 'tusk', 'mk', 'manas']
# filtered_names = list(filter(lambda name: name.startswith('m'), names))

# print(filtered_names)


# numbers = [1, 2, 3, 4, 8, 10]
# filtered_numbers=list(filter(lambda number: number % 4 ==0, numbers))

# print(filtered_numbers)

# dict1=[{'vooker': 'aganim', 'point': 4200},
#         {'vooker': 'hex', 'point': 5700},
#         {'vooker': 'aganim', 'voker': 'refresh'}]
# dict_new=list(filter(lambda x: x['vooker'] == 'aganim', dict1))
# print(dict_new)


# users = [{'username': 'kuba', 'buyback': ['yes']},   -> определение у кого выкуп естьь )
#         {'username': 'bekon', 'buyback': []}]

# imba=list(filter(lambda x: x.get('buyback', None), users))
# lax=list(filter(lambda x: not x['buyback'], users))
# print(f'good {imba}')
# print(f'bad {lax}')


# names = ['Kuba', 'Pudge', 'Voker', 'Tusk']
# greetings = list(map(lambda name: f'Welcoome: {name}', filter(lambda x: len(x)>=5, names))) -> комбо map+lambda+filter
# print(greetings)



# ////////// reduce(func, iterable object)////////////////

# import functools

# numbers=[1, 2, 3, 4]
# sum_=functools.reduce(lambda x, y: x+y, numbers)
# print(sum_)

# numbers = [78, 34, -4, 0, 3334, 543]
# max_=functools.reduce(lambda a, b: a if a>b else b, numbers) # -> тут тоже так как в тетради. после каждый сравнение в "а" записовается наибольший значение и в конце reduce выводит нам единичный результат
# print(max_)

# from functools import reduce

# numbers=[5, 6, 3, 8]
# mutiply=reduce(lambda x, y: x*y, numbers)
# print(mutiply)


# ////////////// zip() //////////

# list1=[1, 2, 3, 4, 5]
# list2=['a', 'b', 'c', 'd', 'e']
# list3=['kub', 'voker']
# zipped_list=list(zip(list1, list2, list3)) # -> тут можно не только на список можно оборачиват но и  на set. а чтоб обернуть на dict нужно только 2 переменных
# print(zipped_list) #  -> [(1, 'a', 'kub'), (2, 'b', 'voker')]  -> так вышло weil list3 состоит только из 2 ух элементов то есть тут смотрят на переменную с самым малыми количествоми элементов и создает столько tuple ов 


# list1=[1, 2, 3, 4, 5]
# list2=['a', 'b', 'c', 'd', 'e']
# list3=[4, 5, 6, 7, 8, 9]
# zipped_list=set(zip(list1, list2, list3))  #-> так можно сделать словарь с помощью zip
# print(zipped_list)  

# list1=[1, 2, 3, 4, 5]
# list2=['a', 'b', 'c', 'd', 'e']
# list3=['kub', 'voker', 'tusk']
# zipped_list=list(zip(list1, list2, list3))
# unzipped=list(zip(*zipped_list))  -> распокавали как в переменной
# print(unzipped)
# # print(zipped_list) 

# list1=[1, 2, 3, 4, 5]
# list2=['a', 'b', 'c', 'd', 'e']
# list3=['kub', 'voker', 'tusk']
# zipped_list=list(zip(list1, list2, list3))
# lists, bukvy, strings=list(zip(*zipped_list))  -> а так полностю распаковали 
# print(lists, bukvy, strings)
# # print(zipped_list) 


# ..... enumerate() ............. -> номер ставит в каждый элемент. тож является одним из способов создать словарь

# seasons = ['spring', 'winter', 'fall', 'summer']
# enumerate_seasons = list(enumerate(seasons, start=1))  -> можно также оборачиват на словарь и множества. и start можно указать с любого и оно идет с лева направо
# print(enumerate_seasons)


# .............. abs -> возращает обсолюьное значение числа
 
# negative = -2
# absolute=abs(negative)
# print(absolute)

# ////////////    all ->похож на and//////// проверят  все элементы на True , False. то есть все должны быть True что бы вывело True иначе будет False
# ............. any ->похож на or.............. также работает как all но наоборот False, True

# list_of_zeros=[0, 3, 2, 1]
# is_true=all(list_of_zeros)
# print(is_true)

# ////////////  ascii //////////

# list1=['makers', 'мейкерс', 23, 0, '$*']
# list2=ascii(list1)
# print(list2)

# .......... ord(), chr() ...........

# print(ord('b'))
# print(chr(98))

# ......... divmod ..... -> деление и остаток

# a=15
# b=7
# print(divmod(a, b))

# ...........РАЗБОР ТАСКА...................... 
"""
1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
"""
# import functools

# numbers=[1, 2, 3, 4]
# sum_=functools.reduce(lambda x, y: x+y, numbers)
# print(sum_)

"""
2) Дан списка из чисел. Проверьте, что все числа больше трёх.
"""
# numbers = [1, 2, 3, 4, 8, 10]
# filtered_numbers=list(filter(lambda number: number > 3, numbers))

# print(filtered_numbers)

"""
3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
"""
# numbers = [1, 2, 3, 4, 8, 10, -1, -4, -7]
# filtered_numbers=list(filter(lambda number: number < 0, numbers))

# print(filtered_numbers)
"""
4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
"""
# number = [1, 2, 3, 4, 5, 6]
# a = list(map(lambda x:x**2,number))
# print(a)
"""
5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
"""
# numbers = [1, 2, 3, 4, 8, 10]
# filtered_numbers=list(filter(lambda number: number % 2 ==0, numbers))

# print(filtered_numbers)
"""
6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
"""
# numbers = ['kuba', 'boss', 'kubamanasov', 'asdasdasdasdasd']
# filtered_numbers=list(filter(lambda number: len(number)>7 , numbers))

# print(filtered_numbers)

"""
7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
"""
# list_ = [5, 6, 7, 8]
# from functools import reduce
# list2 = reduce(lambda a,b: a*b, list_)
# print(list2)

"""
8) Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
"""
# numbers = [1, 2, 3, 4, 5, 6, 7]
# chet=len(list(filter(lambda a: a % 2 == 0, numbers)))
# nechet=len(list(filter(lambda a: a % 2 == 1, numbers)))
# print(f'количест')
"""
9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0,
 замените его на False, если больше, то на True .
"""

"""
10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
# import functools

# numbers = ['kuba', 'boss', 'kubamanasov']
# filtered_numbers=functools.reduce(lambda a, b: a if len(a)>len(b) else b, numbers)

# print(filtered_numbers)


# ............... РАЗБОР С   АДИЛЕТОМ .......................


#  встроенные функции

# any(iterable) - проверяет что хотя бы один елемент последовательности  является истенным 
# all(iterable) - наоборот

# bool(obj) - True или False исходя из значение обьекта
# bool('') -> False
# bool(0) -> False
# bool(-1.5) -> True
# bool([0]) -> True


# enumerate(iterable, start=0) - прономерировает элементы последовательности

# a=['a', 'b', 'c', 'd']
# res=enumerate(a, 1) -> так он возращает обьект
# print(res) -> <enumerate object at 0x7f58dd1c3c00>

#  # DIVMOD
# divmod(num1, num2)
# (num1 // num2, num1 % num2)
# print(divmod(12.5, 3)) -> (4.0, 0.5)


# ///////////////////   help(obj) - справка пот обьекту //////// 
# ............. с помощью этого кода можно узнать все ...............
# a=10
# help(a)

# id(obj) - возращает адрес памяти
# a=10
# print(id(a))
# a=5
# print(id(a))

# a=83745987357937485793874593234567890987654323456789087654567876545678765456
# print(id(a))
# b=83745987357937485793874593234567890987654323456789087654567876545678765456
# print(id(b))
# print(a is b)

# ...isinstance(obj, class) - проверяет является ли обьект экземпляром данного класса
    # ПРОВЕРКА НА ТИП
# a=10
# isinstance(a, str) -> False
# isinstance(a, int) -> True

# type(obj) -> возращает название класса(тип) к которому относятся обьект


# len({'a': 1, 'b': 2}) -> 2
# len('string') -> 6
# len(range(2,10)) -> 8
# если длина последовательности больше чем 2 ** 31 или 2 ** 61 . то будет ошибка


# max(iterable)
# max(obj, obj2, obj3, [key])

# key - функция . при помощью котрой нужно найти максимальный элемент
# a=['kuba', 'voker', 'oleg', 'tusk']
# max(a) -> 'oleg'
# max(a, key=len) -> 'voker'      -> таким образом используетсяя key в max min функциях
# min(iterable)
# min(obj, obj2, obj3, [key])
# sum(iterable)

