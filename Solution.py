from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        freq_list= []
        for i in range(k):
            freq_list.append(sorted_freq[i][0])
        return freq_list




