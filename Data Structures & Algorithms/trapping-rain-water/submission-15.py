class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        count = 0


        while l < r:
            if l_max < height[l]:
                l_max = height[l]
            
            if r_max < height[r]:
                r_max = height[r]

            if l_max < r_max:
                if l_max > height[l]:
                    count += (l_max - height[l])
                l += 1
            else:
                if r_max > height[r]:
                    count += (r_max - height[r])
                r -= 1

        return count
