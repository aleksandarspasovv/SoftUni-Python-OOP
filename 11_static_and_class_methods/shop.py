class Shop:

    def __init__(self, name, type_shop, capacity):
        self.name = name
        self.type = type_shop
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type_shop):
        return cls(name, type_shop, 10)

    def add_item(self, item_name):
        try:
            