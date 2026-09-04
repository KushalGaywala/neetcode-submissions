class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ("(", "{", "[")
        closings = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for i in range(len(s)):
            if s[i] in openings:
                stack.append(s[i])
            elif stack and stack[-1] == closings[s[i]]:
                stack.pop()
            else:
                return False

        return stack == []
