class TimeMap:

    def __init__(self):
        '''
        map to store
        key: list of values [value, timestamp]
        '''
        self.timeValueMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeValueMap:
            self.timeValueMap[key] = []
        
        self.timeValueMap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #time value map is a list of values
        #[[happy,1], [sad,2], [xyz,3]]
        values = self.timeValueMap.get(key, [])


        l, r = 0, len(values)-1

        while l<=r:
            mid = l+(r-l)//2

            #retrieve middle list within our list of values
            #access the second element which has the timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1
            
        return res
        
