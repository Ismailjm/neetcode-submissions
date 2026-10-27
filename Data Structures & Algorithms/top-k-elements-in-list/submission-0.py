from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occurences = defaultdict(list)
        for num in nums:
            num_occurences[num].append(num)
        # print(sorted(num_occurences.items()))
        num_occurences_sorted = dict(sorted(num_occurences.items(), key=lambda item: len(item[1])))
        top_frequent = list(num_occurences_sorted.keys())[::-1]
        print(top_frequent)
        return top_frequent[:k]