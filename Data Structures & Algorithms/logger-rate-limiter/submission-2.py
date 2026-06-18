class Logger:

    def __init__(self):
        '''
        Use a hash map to store the last printed timestamp for each message.

        The idea is:
        - message -> last time it was printed
        - if we have never seen the message before, we can print it
        - if we have seen it before, only print it if at least 10 seconds have passed

        TC: O(1) per call on average, because dictionary lookup/update is constant time
        SC: O(m), where m is the number of unique messages stored
        '''
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If this message has never been printed before, print it and store its timestamp.
        if message not in self.last_printed:
            self.last_printed[message] = timestamp
            return True
        
        # If the message was printed before, check whether 10 seconds have passed.
        if timestamp >= self.last_printed[message] + 10:
            # Update the last printed time because we are printing it again now.
            self.last_printed[message] = timestamp
            return True
        
        # Otherwise, it is too soon to print the same message again.
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp, message)