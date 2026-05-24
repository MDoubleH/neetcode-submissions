class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Use a stack because Reverse Polish Notation is evaluated from left to right

        The idea is:
        - if we see a number, push it onto the stack
        - if we see an operator, pop the last two numbers from the stack
        - apply the operator
        - push the result back onto the stack

        This works because in RPN, the operator always applies to the two most recent numbers

        For addition and multiplication:
        - order does not matter
        - so we can directly pop both values and apply the operation

        For subtraction and division:
        - order does matter
        - the second popped value is actually the right operand
        - the first popped value is actually the left operand

        Example:
        tokens = ["4", "13", "5", "/", "+"]
        stack becomes:
        - push 4
        - push 13
        - push 5
        - "/" means 13 / 5
        - push result
        - "+" means 4 + result

        At the end:
        - the stack should contain one value
        - that value is the final answer

        TC: O(n), where n is the number of tokens
        - we process each token once
        - stack operations are O(1)

        SC: O(n)
        - in the worst case, many numbers are pushed onto the stack before operators appear
        '''

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                # For subtraction, order matters
                # a is the right operand, b is the left operand
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                # For division, order matters
                # Need b / a, not a / b
                # int() truncates toward zero, which matches the problem requirement
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                # Token is a number, so convert it to int and push onto the stack
                stack.append(int(token))

        return stack[-1]