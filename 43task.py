#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def unique(args):
    uniques = [i for i in args if args.count(i) == 1]
    return uniques
    

list = [randint(0, 20) for i in range(randint(10, 15))] 
print(f' Дана последовательность чисел: {list}')
print(f' Cписок уникальных элементов заданной последовательности: {unique(list)}')