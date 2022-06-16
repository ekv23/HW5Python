#В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def numbers(link):
    data = open(link, 'r')
    list_numbers = data.read() + ' '
    list_numbers = list(map(int, list_numbers.split()))
    data.close
    return list_numbers

def find_number(list):
    number = ''
    for i in range(len(list)):
        if not list[i] - 1 == list[i-1]:
            number = list[i]-1
    return number

path = '/Users/ekaterina/Desktop/Desktop/Python/lesson5/35/file.txt'
sequence = numbers(path)

print(f'Натуральные числа из файла: {sequence}')
print(f'Найденное число: {find_number(sequence)}')
