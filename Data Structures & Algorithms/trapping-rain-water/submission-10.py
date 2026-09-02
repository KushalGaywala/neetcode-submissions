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

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# while l < r:
#     l = 0; h[l] = 0
#     r = 9; h[r] = 1

#     if lm < l;
#         lm = h[l] = 0; 

#     if min(lm, rm) = lm = 0; # then left is computed
#         h[l] = 0; lm = 0;
#         if lm - h[l] > 0: # here 0 - 0 > 0 is False so no count increment and move one right
#             count += (lm - h[l])
#         l += 1
#     else:
#         if rm < r;
#             lr = h[r] = 1;

#         h[r] = 0; rm = 0;
#         if rm - h[r] > 0: # here 0 - 0 > 0 is False so no count increment and move one left
#             count += (rm - h[r])
#         r -= 1

#     l = 1; h[l] = 2






    