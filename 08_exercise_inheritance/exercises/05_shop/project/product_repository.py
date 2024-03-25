from project.drink import Drink
from project.food import Food


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        # for product in self.products:
        #     if product.name == product_name:  # Check for product.name instead
        #         return product
        return next((product for product in self.products if product.name == product_name), None)

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join(f'{p.name}: {p.quantity}' for p in self.products)
