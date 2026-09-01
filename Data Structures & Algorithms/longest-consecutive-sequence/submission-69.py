class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        higest_count = 0

        numset = set(nums)

        for i in range(len(nums)):
            current = 0
            if nums[i] - 1 not in numset:
                current = nums[i]
                while current + 1 in numset:
                    current += 1
                
                higest_count = max(higest_count, current - nums[i] + 1)

        return higest_count
