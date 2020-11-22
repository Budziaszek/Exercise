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
                         self.s_s.sum("SpendAmount",  distinct=True, filter_key="SpendAmount",
                                      condition=lambda x: x > 50))


if __name__ == '__main__':
    unittest.main()
