# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Have a dummy node and a curr node
        dummy keeps track of head whihc is what we will return at the end 
        curr will keep track of our position and building the ll

        go through list1 and 2 while they both have elements
        curr.next will equal which ever node is smaller
        Move curr and the whichever list node we chose, 1 ahead so we keep moving forwards

        When we reached the end of either list, we exit the loop
        curr.next will equal the rest of whatever list remains 

        we then return dummy.next as that is the beginning of the list
        '''
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2=list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next
                