class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for schar in s:
            count[schar] = count.get(schar, 0) + 1

        for tchar in t:
            if tchar not in count:
                return False
            count[tchar] -= 1
            if count[tchar] == 0:
                del count[tchar]

        return len(count) == 0