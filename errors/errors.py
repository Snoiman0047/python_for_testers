
# exe 1

def print_message(value):
    """
    Thread the word OK to the parameter sent (with error handling).
    :param value:
    :return: None
    """
    try:
        message = value + ' - OK'
        print('everything is ok.')
        print(message)
    except TypeError:
        print('there was a type error.')
        message = str(value) + ' - OK'
        print('value after error handling:', message)


print_message(True)
print('\n')

# exe 2

try:
    my_list = [1, 2, 0]
    my_list[6] = my_list[1] / my_list[2]
    print(my_list)
except IndexError:
    print("You list's index is out of bound")
except ZeroDivisionError:
    print("You can't divide number by zero")        # this line will be the output

