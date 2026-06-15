class TimeMap:

    def __init__(self):
        self.time_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        
        self.time_map[key].append([value, timestamp])
         

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        #time value map is a list of values
        #[[happy,1], [sad,2], [xyz,3]]
        values = self.time_map.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0]
                return res
        
        return res
        




