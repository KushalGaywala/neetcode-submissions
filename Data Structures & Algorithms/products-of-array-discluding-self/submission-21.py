class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)

        prefix = [1]*length
        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i-1]

        suffix = [1]*length
        for i in range(length-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(length):
            res.append(prefix[i] * suffix[i])

        return res

