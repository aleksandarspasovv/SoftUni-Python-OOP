class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = {}
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
