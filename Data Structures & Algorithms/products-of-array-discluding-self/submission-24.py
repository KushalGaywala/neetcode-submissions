class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        non_zero_product = 1
        no_of_zeros = 0
        for num in nums:
            product *= num
            if num == 0:
                no_of_zeros += 1
                continue
            non_zero_product *= num
        
        if no_of_zeros >= 2:
                return [0]*len(nums)
        
        res = list()
        for num in nums:
            if num == 0:
                res.append(non_zero_product)
                continue
            res.append(product//num if num != 0 else 0)
        
        return res