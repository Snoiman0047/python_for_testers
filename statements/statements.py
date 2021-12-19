import math

import sympy  # install by terminal (pip3 install mpmath)


def equal_indexes_in_list(_list, _index1, _index2):
    """
    Compare entries in the list according to the indexes and print a message to the console accordingly.
    :param _list:
    :param _index1:
    :param _index2:
    :return: None
    """
    if _list[_index1] > _list[_index2]:
        print("First one is bigger")
    elif numbers[_index1] < numbers[_index2]:
        print("Second one is bigger")
    else:
        print("Both are equal")


def is_prime(_num):
    """
    Check whether the number sent as a parameter is a prime number.
    :param _num:
    :return: Boolean value according to the test result.
    """
    for index in range(2, int(math.sqrt(_num) + 1)):
        if _num % index == 0:
            return False
    return True


# exe 01

x, y = 10, 12
if x == y:
    print('numbers are equals.')
else:
    print('max number is:', max(x, y))
print('\n')


# exe 02

numbers = [2, 5, 9]
print('original list result: ', end='')
equal_indexes_in_list(numbers, 0, 1)
numbers.insert(0, 5)
print('result after list changed: ', end='')
equal_indexes_in_list(numbers, 0, 1)
numbers.insert(0, 8)
print('result after list changed: ', end='')
equal_indexes_in_list(numbers, 0, 1)
print('\n')


# exe 03

print('numbers in range 1-10 (for): ', end='')
for num in range(1, 11):
    print(num, end=', ')
print()

print('numbers in range 1-10 (while): ', end='')
num = 1
while num <= 10:
    print(num, end=', ')
    num += 1
print()

print('even numbers in range 30-50: ', end='')
for num in range(30, 51):
    if num % 2 == 0:
        print(num, end=', ')
print()

print('odd numbers in range 20-40: ', end='')
for num in range(20, 41):
    if num % 2 != 0:
        print(num, end=', ')
print('\n')


# exe 04

countries = ['Austria', 'Germany', 'Canada', 'Peru', 'Israel']

print('countries: ', end='')
for country in countries:
    print(country, end=', ')
print()

if 'Israel' in countries:
    print("Israel is founded in countries list.")

if countries[2] == "China":
    print("Yes, it is there")
else:
    print("No, Sorry...")

print('number of chars in the first country:', len(countries[0]))
print('\n')


# exe 05

age = int(input('please insert your age: '))
if 0 < age <= 6:
    print('Go to Kindergarten')
elif 6 < age <= 18:
    print('Go to School')
elif 18 < age <= 67:
    print('Go to Work')
elif 67 < age <= 20:
    print('Collect your pension')
print('\n')


# exe 06

profession = input('please insert your profession: ')
if profession.lower() == 'teacher':
    salary = 5000
elif profession.lower() == 'bank teller':
    salary = 10000
elif profession.lower() == 'qa':
    salary = 15000
elif profession.lower() == 'average salary':
    salary = 9100
else:
    salary = 'wrong profession'
print('salary is:', salary)
print('\n')


# exe 07

names = {111111111: 'sara', 222222222: 'sima', 333333333: 'israel', 444444444: 'shimon'}
for name in names.keys():
    print('ID:', name)
for name in names.values():
    print('Name:', name)
print('\n')


# exe 08

numbers = {3, 8, 11, 27, 30, 41}
print('numbers in list are divided by 3 and 5 with no remainder: ', end='')
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print(number)
print('\n')


# exe 09

word = ['o', 'l', 'l', 'e', 'h']
print('reverse list: ', end='')
while len(word) > 0:
    print(word.pop(), end='')
print('\n')


# exe 10

numbers = [15, 2, 36, 20, 7]
print('max value: ', end='')
if numbers[0] > numbers[1]:
    if numbers[0] > numbers[2]:
        print(numbers[0])
    else:
        print(numbers[2])
else:
    if numbers[1] > numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])

_max = numbers[0]
for number in numbers:
    if number > _max:
        _max = number
print('max value of list:', _max)

_sum = 0
for number in numbers:
    _sum += number
print("sum of elements in list:", _sum)
print('\n')


# exe 11

num = int(input('please insert any numbers: '))
if is_prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')
print(f'is {num} prime (build-in function): {sympy.ntheory.primetest.isprime(num)}')
