from solution.summary_statistics import SummaryStatistics
from statistics import mean


def main():
    demo()


def get_sample_data(data=((1, 2, 3, 1), (5, 4, 6, 6), (100, 150, 50, 10)),
                    keys=("CustomerId", "ItemId", "SpendAmount")):
    return [{key: item for key, item in zip(keys, items)} for items in zip(*data)]


def demo():
    short_sample_data = get_sample_data()
    s_s = SummaryStatistics(short_sample_data)
    print("Data: {}".format(short_sample_data))
    number_of_transactions = s_s.count("CustomerId")
    number_of_customers = s_s.count("CustomerId", distinct=True)
    total_amount_spent = s_s.sum("SpendAmount")
    total_amount_spent_customer_1 = s_s.sum("SpendAmount", filter_key="CustomerId", condition=lambda x: x == 1)
    mean_amount_spent = s_s.custom_operation(mean, "SpendAmount")
    distinct_item_6_buyers = s_s.count("CustomerId", distinct=True, filter_key="ItemId", condition=lambda x: x == 6)
    customers_who_spend_once_over_50 = s_s.count("CustomerId", distinct=True, filter_key="SpendAmount",
                                                 condition=lambda x: x > 50)
    customers_who_spend_total_over_100 = s_s.count("CustomerId", distinct=True, filter_key="SpendAmount",
                                                   condition=lambda x: x > 100, group_by_key="CustomerId",
                                                   reduce_function=sum)

    print("Number of rows (here number of transactions): {}".format(number_of_transactions))
    print("Number of customers: {}".format(number_of_customers))
    print("Total amount of money spent by all customers: {}".format(total_amount_spent))
    print("Total amount of money spent by customer with CustomerId = 1: {}".format(total_amount_spent_customer_1))
    print("Custom function call (mean of amount of money spent by customers): {}".format(mean_amount_spent))
    print("Count of distinct customers who bought item with ItemId = 6: {}".format(distinct_item_6_buyers))
    print("Count of distinct customers who spend on item more than 50: {}".format(customers_who_spend_once_over_50))
    print("Count of customers who spent more than 100 (total): {}".format(customers_who_spend_total_over_100))


if __name__ == "__main__":
    main()
