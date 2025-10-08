from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #print(counter)
        def frequency(x):
            return counter[x]
        values_sorted = sorted(counter.keys(), key = frequency, reverse = True)
        values_to_k = values_sorted[:k]
        #print(listfr)
        return values_to_k
