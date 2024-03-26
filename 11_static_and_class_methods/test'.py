class Points:

    def __int__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_difference(x, y):
        return x - y


class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['parmesan, tomato sauce'])

    def __str__(self):
        return f'{self.ingredients}'


first_pizza = Pizza.pepperoni()
print(first_pizza)
