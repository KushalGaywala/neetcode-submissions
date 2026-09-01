class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        higest_count = 0

        numset = set(nums)

        for num in numset:
            current = 0
            if num - 1 not in numset:
                current = num
                while current + 1 in numset:
                    current += 1
                
                higest_count = max(higest_count, current - num + 1)

        return higest_count
