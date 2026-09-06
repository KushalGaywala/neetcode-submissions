class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        diff = {}

        for char in s1:
            diff[char] = diff.get(char, 0) + 1

        for r in range(len(s2)):
            diff[s2[r]] = diff.get(s2[r], 0) - 1
            if diff[s2[r]] == 0:
                del diff[s2[r]]

            if r - l + 1 > len(s1):
                diff[s2[l]] = diff.get(s2[l], 0) + 1
                if diff[s2[l]] == 0:
                    del diff[s2[l]]
                l += 1

            if r - l + 1 == len(s1) and not diff:
                return True

        return False