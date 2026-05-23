class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Use a stack because brackets must be closed in the reverse order
        that they were opened

        This is a LIFO problem:
        - the last opening bracket we see must be the first one to close

        close_to_open maps each closing bracket to the opening bracket it needs

        Go through each character in s:
        - if it is an opening bracket, add it to the stack
        - if it is a closing bracket, check whether it matches the top of the stack

        When we see a closing bracket:
        - the stack must not be empty
        - the top of the stack must be the matching opening bracket
        - if both are true, pop from the stack
        - otherwise, return False

        At the end:
        - if the stack is empty, every opening bracket was matched correctly
        - if the stack still has values, some brackets were never closed

        TC: O(n), where n is the length of s
        - we go through each character once
        - stack operations are O(1)

        SC: O(n)
        - in the worst case, all characters are opening brackets and stored in the stack
        '''

        close_to_open = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            else:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack