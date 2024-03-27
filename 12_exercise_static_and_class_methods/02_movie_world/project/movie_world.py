from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    