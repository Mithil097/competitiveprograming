def get_max_profit(stock_prices):

    # Calculate the max profit
    if len(stock_prices) < 2:
        raise ValueError("should be greater than2")
    else:
        minpri  = stock_prices[0]
        maxpro = stock_prices[1] - stock_prices[0]
        for current_time in range(1, len(stock_prices)):
            current_pri = stock_prices[current_time]
            expected_pro = current_pri - minpri
            maxpro = max(maxpro, expected_pro)
            minpri  = min(minpri, current_pri)
    
        return maxpro



    return 0


















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)