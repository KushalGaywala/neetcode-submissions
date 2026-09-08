class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        mid = end // 2

        while True:
            if start > end:
                return -1

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
                mid = start + (end - start) // 2
            else:
                end = mid - 1
                mid = start + (end - start) // 2
        
        return -1



# n = -1, 0, 3, 5, 9, 12
# t = 12

# s = 3
# e = 6 # n[s] < t; length

# n[s] < t; 5 < 12
# l = 3
# e = 3
# s = 3 + 3 // 2; 3 + 1; 4

# n[s] < t; 9 < 12
# l = 1
# e = 4
# s = 4 + 4 // 2; 4 + 2; 6





# n = [-1, 0, 2, 4, 6, 8]
# t = 4

# s = 2
# e = 6

# n[s] < t; 2 < 4

# l = 6-2; 4
# e = 2
# s = 2 + (4 // 2); 2 + (2 // 2); 3

# n[s] < t; 4 == 4; return s; 4 < 4


# not found example
# n = [0, 1, 2, 4, 6, 8]
# t = -1

# s = 2
# e = 0

# n[s] < t; 2 < -1; false

# l = 0 - 2 = -2
# e = 2
# s = 2 // 2 = 1

# n[s] < t; 1 < -1; false
# e = 1
# s = 1 // 2 = 0

# n[s] < t; 0 < -1; false; e == s; return -1

# n[s] < t; 4 == 4; return s; 4 < 4



# not found example
# n = [-1, 0, 2, 4, 6, 8]
# t = 3

# s = 2
# e = 6

# n[s] < t; 2 < 3; true
# e = 2
# s = 2 + (4 // 2) = 4

# n[s] < t; 6 < 3; false
# e = 6
# s = 6 // 2 = 3

# n[s] < t; 4 < 3; false
# e = 3
# s = 3 // 2 = 1

# n[s] < t; 1 < 3; true
# e = 1
# s = 1 + (1 - 1 // 2) = 1

# n[s] < t; 0 < 0; false; e == s; 1 == 1; return -1

# n[s] < t; 4 == 4; return s; 4 < 4


