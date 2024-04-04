from unittest import TestCase, main

#from exercises.car_manager import Car


class TestCar(TestCase):
    pass

    def setUp(self) -> None:
        self.car_manager = Car('Nissan', 'GT-R', 20, 75)

    def test_init(self):
        self.assertEqual('Nissan', self.car_manager.make)
        self.assertEqual('GT-R', self.car_manager.model)
        self.assertEqual(20, self.car_manager.fuel_consumption)
        self.assertEqual(75, self.car_manager.fuel_capacity)
        self.assertEqual(0, self.car_manager.fuel_amount)

    def test_cannot_be_empty_string(self):
        with self.assertRaises(Exception) as es:
            self.car_manager.make = ''

        self.assertEqual("Make cannot be null or empty!", str(es.exception))

    def test_model_cannot_be_empty_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cannot_be_negattive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_cannot_be_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_amount_cannot_be_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_works_properly(self):
        self.car_manager.fuel_capacity = 75
        self.car_manager.refuel(80)
        self.assertEqual(75, self.car_manager.fuel_capacity)


if __name__ == '__main___':
    main()
