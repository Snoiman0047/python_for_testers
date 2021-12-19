
# exe_1

print('please insert your-')
first_name = input('first name: ')
last_name = input('last name: ')
age = int(input('age: '))

age = str(age)

print('*   ' * 4)
print(first_name.upper(), last_name.lower())

print('first char in your first name:', first_name[0])
print('last char in your last name:', last_name[-1])
print('\n')


# exe_2

sentence = 'Python is a general purpose computer programming language'
print('amount of occurrences of the word in a sentence:', sentence.count('computer'))
print('index of the word in the sentence:', sentence.find('computer'))
print('sentence without spaces:', sentence.replace(' ', ''))
print('\n')


#  exe_3

sentence = 'Hello World'
print('last word in sentence:', sentence[sentence.find(' ') + 1:])
print('\n')