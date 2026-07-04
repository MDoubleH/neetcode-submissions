class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        stack = []

        for c in s:
            if c in close_to_open:
                if not stack or close_to_open[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True

