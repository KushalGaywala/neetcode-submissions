class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        r = 0
        count = 0
        max_count = 0
        seq = set()

        while l <= r < len(s):
            if s[r] in seq:
                seq.remove(s[l])
                l += 1
                count -= 1
            else:
                seq.add(s[r])
                count += 1
                r += 1

            max_count = max(max_count, count)

        return max_count
        