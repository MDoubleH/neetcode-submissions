class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Use sorting + a stack/list to track fleet arrival times.

        The idea is:
        - pair each car's position with its speed
        - sort cars from closest to target to furthest from target
        - calculate how long each car takes to reach the target
        - if a car behind takes less or equal time than the fleet ahead,
          it catches up and becomes part of that fleet
        - if it takes longer, it cannot catch the fleet ahead, so it forms a new fleet

        This works because once we process cars from front to back,
        each car only needs to compare with the fleet directly ahead of it.

        TC: O(n log n), where n is the number of cars, because of sorting
        SC: O(n), because we store the cars and fleet times
        '''
        cars = []

        # Pair each car's position with its speed.
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # Sort from closest to the target to furthest from the target.
        # Python sorts tuples by the first value first, so this sorts by position.
        cars.sort(reverse=True)

        # fleet stores the arrival time of each fleet.
        # The last value is the fleet directly ahead of the current car.
        fleet = []

        for pos, spe in cars:
            # time = distance / speed
            distance = target - pos
            time = distance / spe

            # If this car takes longer than the fleet ahead,
            # it cannot catch up, so it starts a new fleet.
            if not fleet or time > fleet[-1]:
                fleet.append(time)

            # Otherwise, this car catches the fleet ahead,
            # so we do not add a new fleet.
        
        return len(fleet)