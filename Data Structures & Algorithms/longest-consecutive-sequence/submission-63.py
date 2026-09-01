class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(set)
        higest_count = 0
        count = 0
        current = 0

        numset = set(nums)

        for i in range(len(nums)):
            current = 0
            if nums[i] - 1 not in numset:
                current = nums[i]
                count = 1
                while current + 1 in numset:
                    count += 1
                    current += 1
                
            if higest_count < count:
                higest_count = count

        return higest_count
