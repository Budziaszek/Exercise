from collections import defaultdict
from itertools import groupby
from typing import List
from collections.abc import Iterable

SummaryStatisticsData = List[dict]


class SummaryStatistics:

    def __init__(self, data: SummaryStatisticsData = None):
        self.data = data

    def _get_by_key(self, key, filter_key=None, condition=lambda x: True, data=None):
        if data is None:
            data = self.data
        for item in data:
            if filter_key is None or condition(item[filter_key]):
                yield item[key]

    @staticmethod
    def _group(data, key):
        grouped = groupby(sorted(data, key=lambda x: x[key]), key=lambda x: x[key])
        res = list()
        for group, items in grouped:
            d = defaultdict(list)
            for item in items:
                for item_key in item:
                    d[item_key].append(item[item_key])
            d[key] = group
            res.append(dict(d))
        return res

    @staticmethod
    def _reduce(data, reduce_function=sum):
        for item in data:
            for item_key in item:
                if isinstance(item[item_key], Iterable):
                    item[item_key] = reduce_function(item[item_key])
        return data

    def _group_by(self, key, reduce_function=sum):
        res = self._group(self.data, key)
        return self._reduce(res, reduce_function)

    def sum(self, key, distinct=False, filter_key=None, condition=None, group_by_key=None):
        data = self._group_by(group_by_key) if group_by_key else self.data
        if not distinct:
            return sum(self._get_by_key(key, filter_key, condition, data=data))
        return sum(set(self._get_by_key(key, filter_key, condition, data=data)))

    def count(self, key, distinct=False, filter_key=None, condition=None, group_by_key=None):
        data = self._group_by(group_by_key) if group_by_key else self.data
        res = self._get_by_key(key, filter_key, condition, data=data)
        return len(list(res) if not distinct else set(res))

    def custom_operation(self, fun, key, distinct=False, filter_key=None, condition=None, group_by_key=None):
        data = self._group_by(group_by_key) if group_by_key else self.data
        res = self._get_by_key(key, filter_key, condition, data=data)
        return fun(list(res) if not distinct else set(res))



