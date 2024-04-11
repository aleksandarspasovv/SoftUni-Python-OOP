from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        result = reduce(lambda x, y: x + y, args)
        return result

    @staticmethod
    def multiply(*args):
        result = reduce(lambda x, y: x * y, args)
        return result

    @staticmethod
    def divide(*args):
        result = reduce(lambda x, y: x / y, args)
        return float(result)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
