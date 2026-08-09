class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Map each closing bracket to its matching opening bracket.
        2. Loop through s:
           - If it's an opening bracket, push it onto the stack.
           - If it's a closing bracket, check that the top of the stack
             contains its matching opening bracket.
           - If not, return False. Otherwise, pop it.
        3. At the end, the stack must be empty for the string to be valid.

        TC: O(n), where n is the length of s.
        SC: O(n) in the worst case.
        """

        close_to_open = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for bracket in s:
            if bracket in close_to_open:
                if stack and stack[-1] == close_to_open[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack