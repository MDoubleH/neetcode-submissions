class RandomizedSet:
    '''
    We can only get random from a list array because it is ordered and has indexes
    So we use a hashmap for o(1) time operations, this will handle insertions and removals

    random: use random function provided by python on the array.
    insert: 
    if item is present in hashmap then just return false
    Else:
    - We must insert in the hashmap, the value and its index
    - We also add the value to the array, it being added to end of array so it's o(1)
    the index of hashmap is simply the length of the list - 1
    - return False

    Deletion:
    if item not in hashmap, return False
    ELSE:
    - To delete in o(1) time from an array we must delete from the end of an array
    - We simply get the index of deleted val from hashmap, the last val in our array must replace the deleted val
    - We delete the deleted val from our hashmap + reduce length of array - should be done with just popping from array
    - We update index of the last elem to whatever index we moved it to 
    return True
    '''

    def __init__(self):
        self.nums_map = {}
        self.nums_array = []
        

    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
        else:
            self.nums_array.append(val)
            self.nums_map[val] = len(self.nums_array)-1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.nums_map:
            return False
        else:
            deleted_val_index = self.nums_map[val]
            last_elem = self.nums_array[-1]
            self.nums_map[last_elem] = deleted_val_index
            self.nums_array[deleted_val_index] = last_elem
            self.nums_array.pop()
            del self.nums_map[val]
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums_array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()