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
