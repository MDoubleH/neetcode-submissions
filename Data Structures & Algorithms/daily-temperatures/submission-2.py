class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Monotonic decreasing stack where we keep track of temps

        2 stacks 
        1. Keep track of indexes and current hottest temp
        2. Result array that contains all 0's that will be filled in if we find a warmer temp

        Go through array temperatures, while we have items in our stack aka temps and the current temp is warmer 
        We calculate the difference in days aka index positions between the two temps and store it in result array
        then at the end of the loop just add new temp to the stack

        Return the resultant array
        '''

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return res
        







