from statistics import mean

from solution.summary_statistics import SummaryStatistics
import unittest
from solution.app import get_sample_data


class TestSummaryStatistics(unittest.TestCase):
    s_s = SummaryStatistics()

    def test_sum(self):
        data_customers, data_items, data_amounts = ((1, 2, 3, 1), (5, 4, 6, 6), (100, 150, 50, 10))
        self.s_s.data = get_sample_data(data=(data_customers, data_items, data_amounts),
                                        keys=("CustomerId", "ItemId", "SpendAmount"))
        self.assertEqual(sum(data_amounts), self.s_s.sum("SpendAmount"))
        self.assertEqual(sum(data_items), self.s_s.sum("ItemId"))
        self.assertEqual(sum(data_customers), self.s_s.sum("CustomerId"))
        self.assertEqual(sum([d for d in data_amounts if d > 50]), self.s_s.sum("SpendAmount", filter_key="SpendAmount",
                                                                                condition=lambda x: x > 50))
        self.assertEqual(sum(set(data_amounts)), self.s_s.sum("SpendAmount", distinct=True))
        self.assertRaises(ValueError, self.s_s.sum, "SpendAmount", filter_key="SpendAmount", distinct=True)
        self.assertRaises(ValueError, self.s_s.sum, "SpendAmount", condition=lambda x: x > 50, distinct=True)
        self.assertEqual(sum(set([d for d in data_amounts if d > 50])),
                         self.s_s.sum("SpendAmount", distinct=True, filter_key="SpendAmount",
                                      condition=lambda x: x > 50))
        self.assertEqual(110, self.s_s.sum("SpendAmount", filter_key="CustomerId", condition=lambda x: x == 1))
        self.assertEqual(150, self.s_s.sum("SpendAmount", filter_key="CustomerId", condition=lambda x: x == 2))

    def test_count(self):
        data_customers, data_items, data_amounts = ((1, 2, 3, 1), (5, 4, 6, 6), (100, 150, 50, 10))
        self.s_s.data = get_sample_data(data=(data_customers, data_items, data_amounts),
                                        keys=("CustomerId", "ItemId", "SpendAmount"))
        self.assertEqual(len(data_amounts), self.s_s.count("SpendAmount"))
        self.assertEqual(len(data_items), self.s_s.count("ItemId"))
        self.assertEqual(len(data_customers), self.s_s.count("CustomerId"))
        self.assertEqual(len([d for d in data_amounts if d > 50]),
                         self.s_s.count("SpendAmount", filter_key="SpendAmount", condition=lambda x: x > 50))
        self.assertEqual(len(set(data_amounts)), self.s_s.count("SpendAmount", distinct=True))
        self.assertRaises(ValueError, self.s_s.count, "SpendAmount", filter_key="SpendAmount", distinct=True)
        self.assertRaises(ValueError, self.s_s.count, "SpendAmount", condition=lambda x: x > 50, distinct=True)
        self.assertEqual(len(set([d for d in data_amounts if d > 50])),
                         self.s_s.count("SpendAmount", distinct=True, filter_key="SpendAmount",
                                        condition=lambda x: x > 50))
        self.assertEqual(2, self.s_s.count("SpendAmount", filter_key="CustomerId", condition=lambda x: x == 1))
        self.assertEqual(1, self.s_s.count("SpendAmount", filter_key="CustomerId", condition=lambda x: x == 2))

    def test_custom_operation(self):
        data_customers, data_items, data_amounts = ((1, 2, 3, 1), (5, 4, 6, 6), (100, 150, 50, 10))
        self.s_s.data = get_sample_data(data=(data_customers, data_items, data_amounts),
                                        keys=("CustomerId", "ItemId", "SpendAmount"))
        self.assertEqual(mean(data_amounts), self.s_s.custom_operation(mean, "SpendAmount"))
        self.assertEqual(mean(data_items), self.s_s.custom_operation(mean, "ItemId"))
        self.assertEqual(mean(data_customers), self.s_s.custom_operation(mean, "CustomerId"))
        self.assertEqual(mean([d for d in data_amounts if d > 50]),
                         self.s_s.custom_operation(mean, "SpendAmount", filter_key="SpendAmount",
                                                   condition=lambda x: x > 50))
        self.assertEqual(mean(set(data_amounts)), self.s_s.custom_operation(mean, "SpendAmount", distinct=True))
        self.assertRaises(ValueError, self.s_s.custom_operation, mean, "SpendAmount", filter_key="SpendAmount",
                          distinct=True)
        self.assertRaises(ValueError, self.s_s.custom_operation, mean, "SpendAmount", condition=lambda x: x > 50,
                          distinct=True)
        self.assertEqual(mean(set([d for d in data_amounts if d > 50])),
                         self.s_s.custom_operation(mean, "SpendAmount", distinct=True, filter_key="SpendAmount",
                                                   condition=lambda x: x > 50))
        self.assertEqual(55, self.s_s.custom_operation(mean, "SpendAmount", filter_key="CustomerId",
                                                       condition=lambda x: x == 1))
        self.assertEqual(150, self.s_s.custom_operation(mean, "SpendAmount", filter_key="CustomerId",
                                                        condition=lambda x: x == 2))


if __name__ == '__main__':
    unittest.main()
