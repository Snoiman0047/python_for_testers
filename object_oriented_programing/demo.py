class Demo:

    @staticmethod
    def handle_numbers(numbers):
        print('The minimum number in list: ' + str(Demo.get_minimum(numbers)))
        print('The maximum number in list: ' + str(Demo.get_maximum(numbers)))
        print('The average number in list: ' + str(Demo.get_average(numbers)))

    @staticmethod
    def get_minimum(numbers):
        return min(numbers)

    @staticmethod
    def get_maximum(numbers):
        return max(numbers)

    @staticmethod
    def get_average(numbers):
        return sum(numbers) / len(numbers)


Demo.handle_numbers([5, 2, 3, 9])