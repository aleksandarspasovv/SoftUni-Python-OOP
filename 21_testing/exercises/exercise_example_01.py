from unittest import TestCase, main
from exercises.integerlist import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init(self):
        self.assertListEqual([1, 2, 3], self.i_list.get_data())

    def test_element_add(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_adds_the_int(self):
        expected_list = self.i_list.get_data() + [4]
        self.i_list.add(4)
        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_ind_with_out_of_range_ind_raises_out_of_ind_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_ind_with_valid_ind(self):
        self.i_list.remove_index(1)

        self.assertEqual([1, 3], self.i_list.get_data())

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_(self):
        result = self.i_list.get(1)
        self.assertEqual(2, result)

    def test_insert_on_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 1000)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_element_not_intiger_insert_raises_element(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 'hello')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_in_a_sorted_list(self):
        expected_list = self.i_list.get_data().conpy()
        expected_list.insert(1, 5)

        self.i_list.insert(1, 5)

        self.assertEqual(expected_list, self.i_list.get_data())







if __name__ == "__main__":
    main()
