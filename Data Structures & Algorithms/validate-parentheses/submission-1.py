class Solution:
    def isValid(self, s: str) -> bool:
        '''
        We want to keep a stack of open brackets
        soon as we see a closed bracket, we check to see if it matches the most recent open bracket
        This is important and useful since we are using the LIFO structure of stacks to see correct ordering of brackets
        We simply compare close bracket to the mapping of open brakcet in stack
        If it matches the open bracket then great, simply pop and continue
        At the end we return True if stack empty else false
        Have a hashmap to map open to close brackets

        TC: O(n) as we go through all of s
        SC: O(n) as it can be all open brackets in our stack

        '''

        stack = []
        openToClose = {"(":")", "[":"]", "{":"}"}

        for bracket in s:
            if bracket in openToClose:
                stack.append(bracket)
            else:
                if stack and openToClose[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True
            