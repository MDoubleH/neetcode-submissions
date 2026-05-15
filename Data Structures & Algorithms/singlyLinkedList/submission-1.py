class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        
        return -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            #So if curr.next (our target) is tail
            if not curr.next.next:
                self.tail = curr
            
            curr.next = curr.next.next
            return True
        
        return False
            
    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
