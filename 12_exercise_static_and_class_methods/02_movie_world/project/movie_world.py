from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []


    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):

        customer = next(filter(lambda c: c.name == customer_id, self.customers))
        dvd = next(filter(lambda d: d.name == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):

        customer = next(filter(lambda c: c.name == customer_id, self.customers))
        dvd = next(filter(lambda d: d.name == dvd_id, self.dvds))

        if dvd not in customer.rented_dvds:

            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)

        return f"{customer.name} has successfully returned {dvd.name}"

