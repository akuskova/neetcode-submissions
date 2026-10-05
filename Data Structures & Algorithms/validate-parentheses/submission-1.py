class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {'[':']', '(':')', '{':'}'}
        stack = []
        for char in s:
            if char in symbols:
                stack.append(char)
            else:
                if stack:
                    if symbols[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0