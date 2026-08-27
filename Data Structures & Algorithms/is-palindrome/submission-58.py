class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i])+32)
            if 'A' <= s[j] <= 'Z':
                s[j] = chr(ord(s[j])+32)

            if not (('a' <= s[i] <= 'z') or ('0' <= s[i] <= '9')):
                i += 1
                continue
            if not (('a' <= s[j] <= 'z') or ('0' <= s[j] <= '9')):
                j -= 1
                continue

            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True