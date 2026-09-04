class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] in ("(", "{", "["):
                stack.append(s[i])
            elif s[i] in (")", "}", "]"):
                if stack == []:
                    return False
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop()
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                else:
                    return False

        return stack == []
