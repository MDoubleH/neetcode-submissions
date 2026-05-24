class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Use a monotonic decreasing stack

        The goal is:
        - for each day, find how many days we need to wait until a warmer temperature

        res starts filled with 0s
        - if a day never gets a warmer temperature, it should stay as 0

        stack stores indexes of days where we have not found a warmer future day yet

        The stack is decreasing by temperature
        - this means the temperatures at the indexes in the stack are waiting for a warmer day
        - when we find a warmer temperature, we can resolve previous colder days

        Go through each temperature:
        - if the current temp is warmer than the temp at the top index of the stack,
          then the current day is the next warmer day for that previous index
        - pop that previous index
        - calculate the wait time as current index - previous index
        - keep doing this while the current temp is warmer than stack top

        Then add the current index to the stack because it now needs to find
        a warmer day in the future

        TC: O(n), where n is the length of temperatures
        - each index is pushed onto the stack once
        - each index is popped from the stack at most once

        SC: O(n)
        - in the worst case, temperatures are decreasing, so all indexes stay in the stack
        '''

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            stack.append(i)
        
        return res