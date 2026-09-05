class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashmap = {}
        max_freq = 0
        max_win = 0

        while l <= r and r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq = max(max_freq, hashmap.get(s[r], 0))
            
            if not (((r - l) + 1) - max_freq) <= k:
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1
                l += 1

            r += 1

            max_win = max(max_win, r - l)

        return max_win

# xyyx

# {
#     x: 1;
# }

# s[l] = x; s[r] = x
# {x: 1}
# max_freq = 1
# r += 1; 0 + 1 = 1; 

# s[1] = y
# {x: 1, y: 1}
# max_freq = max(1, 1); 1
# if s[l] != s[r]; x != y; then
#     if (((1 - 0) + 1) - 1) < k; True; then
#         r += 1; r = 2

# s[2] = y
# {x: 1, y: 2}
# max_freq = max(1, 2); 2
# if s[l] != s[r]; x != y; then
#     if (((2 - 0) + 1) - 2) <= k; True; then
#         r += 1; r = 3

# s[3] = x
# {x: 2, y: 2}
# max_freq = max(2, 2); 2
# if 
