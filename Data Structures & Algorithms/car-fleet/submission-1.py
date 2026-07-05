class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        obtain the position and speed of cars, zipped together
        zip together by position as we care for this to be closest to target
        then reverse sort it so we can have it sorted by closest to target
        Calc the time taken to reach target 
        s = d / t -> t = d/s where d would be target - pos
        if we don't have a stack aka a fleet or our time would be greater than stack[-1]
        then add the time to the stack
        return length of array
        '''
        
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        stack = []

        for p,s in cars:
            distance = target - p

            time = distance / s

            if not stack:
                stack.append(time)
            elif stack and time > stack[-1]:
                stack.append(time)
        
        return len(stack)

