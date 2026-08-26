class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        a = 0
        b = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diffs:
                a = diffs[nums[i]]
                b = i
                break
            diffs[nums[i]] = i
            if diff in diffs and diffs.get(diff) != i:
                a = diffs.get(diff)
                b = i
                break
        return [a, b]