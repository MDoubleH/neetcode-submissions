class Logger:

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = timestamp
            return True
        else:
            '''
            If message already exists in our dict
            We must check, is the new message timestamp + 10 greater than old timestamp?
                if yes, return true, update timestamp
                else false, 
            ''' 
            if timestamp >= self.dict[message] + 10:
                self.dict[message] = timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
