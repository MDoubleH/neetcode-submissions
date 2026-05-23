class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{', ')':'(', ']':'['}
        stack = []

        for bracket in s:
            if bracket in mapping:
                if not stack or mapping[bracket]!=stack.pop():
                    return False
            else:
                stack.append(bracket)

        return not stack