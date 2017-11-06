from unittest import TestCase
from src.main import *


class PrimeTestCase(TestCase):
    """Prime decomposition related tests."""

    def test_get_all_prime_factors_for_not_a_number(self):
        """get_all_prime_factors('s') returns []."""
        self.assertEqual(get_all_prime_factors('s'), [])

    def test_get_all_prime_factors_for_negative(self):
        """get_all_prime_factors(-1) returns []."""
        self.assertEqual(get_all_prime_factors(-1), [])

    def test_get_all_prime_factors_for_0(self):
        """get_all_prime_factors(0) returns []."""
        self.assertEqual(get_all_prime_factors(0), [])

    def test_get_all_prime_factors_for_1(self):
        """get_all_prime_factors(1) returns [1]."""
        self.assertEqual(get_all_prime_factors(1), [1])

    def test_get_all_prime_factors_for_2(self):
        """get_all_prime_factors(2) returns [2]."""
        self.assertEqual(get_all_prime_factors(2), [2])

    def test_get_all_prime_factors_for_100(self):
        """get_all_prime_factors(100) returns [2,2,5,5]."""
        self.assertEqual(get_all_prime_factors(100), [2,2,5,5])

    def test_get_unique_prime_factors_with_count_for_not_a_number(self):
        """get_unique_prime_factors_with_count('s') returns [[], []]."""
        self.assertEqual(get_unique_prime_factors_with_count('s'), [[], []])

    def test_get_unique_prime_factors_with_count_for_negative(self):
        """get_unique_prime_factors_with_count(-1) returns [[], []]."""
        self.assertEqual(get_unique_prime_factors_with_count(-1), [[], []])

    def test_get_unique_prime_factors_with_count_for_0(self):
        """get_unique_prime_factors_with_count(0) returns [[], []]."""
        self.assertEqual(get_unique_prime_factors_with_count(0), [[], []])

    def test_get_unique_prime_factors_with_count_for_1(self):
        """get_unique_prime_factors_with_count(1) returns [[1], [1]]."""
        self.assertEqual(get_unique_prime_factors_with_count(1), [[1], [1]])

    def test_get_unique_prime_factors_with_count_for_2(self):
        """get_unique_prime_factors_with_count(2) returns [[2], [1]]."""
        self.assertEqual(get_unique_prime_factors_with_count(2), [[2], [1]])

    def test_get_unique_prime_factors_with_count_for_100(self):
        """get_unique_prime_factors_with_count(100) returns [[2,5],[2,2]]."""
        self.assertEqual(get_unique_prime_factors_with_count(100),
            [[2,5],[2,2]])

    def test_get_unique_prime_factors_with_products_for_not_a_number(self):
        """get_unique_prime_factors_with_products('s') returns []."""
        self.assertEqual(get_unique_prime_factors_with_products('s'), [])

    def test_get_unique_prime_factors_with_products_for_negative(self):
        """get_unique_prime_factors_with_products(-1) returns []."""
        self.assertEqual(get_unique_prime_factors_with_products(-1), [])

    def test_get_unique_prime_factors_with_products_for_0(self):
        """get_unique_prime_factors_with_products(0) returns []."""
        self.assertEqual(get_unique_prime_factors_with_products(0), [])

    def test_get_unique_prime_factors_with_products_for_1(self):
        """get_unique_prime_factors_with_products(1) returns [1]."""
        self.assertEqual(get_unique_prime_factors_with_products(1), [1])

    def test_get_unique_prime_factors_with_products_for_2(self):
        """get_unique_prime_factors_with_products(2) returns [2]."""
        self.assertEqual(get_unique_prime_factors_with_products(2), [2])

    def test_get_unique_prime_factors_with_products_for_100(self):
        """get_unique_prime_factors_with_products(100) returns [4,25]."""
        self.assertEqual(get_unique_prime_factors_with_products(100), [4,25])
