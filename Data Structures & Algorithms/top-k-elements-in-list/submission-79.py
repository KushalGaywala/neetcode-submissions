class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = defaultdict(int)
        freqs = defaultdict(list)
        top_k = []

        for num in nums:
            num_freqs[num] = num_freqs.get(num, 0) + 1

        for num, freq in num_freqs.items():
            freqs[freq].append(num)

        for i in range(len(nums), 0, -1):
            for num in freqs[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

        return top_k