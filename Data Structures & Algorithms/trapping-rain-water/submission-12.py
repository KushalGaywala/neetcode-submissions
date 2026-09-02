class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = 0
        r_max = 0
        count = 0


        while l < r:
            if l_max < height[l] or l == 0:
                l_max = height[l]
            
            if r_max < height[r] or r == len(height) - 1:
                r_max = height[r]

            if l_max <= r_max:
                if l_max > height[l]:
                    count += (l_max - height[l])
                l += 1
            else:
                if r_max > height[r]:
                    count += (r_max - height[r])
                r -= 1

        return count
