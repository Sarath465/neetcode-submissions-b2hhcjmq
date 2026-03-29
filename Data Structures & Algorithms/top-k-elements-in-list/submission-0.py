class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_d = {}
        for i in nums:
            freq_d[i] = freq_d.get(i,0)+1
        sorted_freq_d = dict(sorted(freq_d.items(), key=lambda x: x[1], reverse=True))
        print(sorted_freq_d)
        return list(sorted_freq_d.keys())[:k]