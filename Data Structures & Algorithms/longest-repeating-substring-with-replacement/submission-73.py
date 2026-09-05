class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashmap = {}
        max_win = 0

        while l <= r and r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            
            if not (((r - l) + 1) - max(hashmap.values())) <= k:
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1
                l += 1

            r += 1

            max_win = max(max_win, r - l)

        return max_win
