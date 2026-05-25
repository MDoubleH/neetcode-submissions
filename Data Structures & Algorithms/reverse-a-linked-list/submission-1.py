# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use three pointers to reverse the linked list in-place

        prev represents the previous node
        - this will become the new next pointer for the current node
        - starts as None because the original head will become the new tail

        curr represents the node we are currently reversing
        - starts at head

        At each step:
        - store curr.next first so we do not lose the rest of the list
        - reverse curr.next to point backwards to prev
        - move prev forward to curr
        - move curr forward to the saved next node

        Once curr becomes None, we have reached the end of the original list
        At that point, prev points to the new head of the reversed list

        TC: O(n), where n is the number of nodes
        - we visit each node once

        SC: O(1)
        - we reverse the list in-place using only a few pointer variables
        '''

        prev = None
        curr = head

        while curr:
            next_node = curr.next      # save the rest of the list
            curr.next = prev           # reverse the pointer
            prev = curr                # move prev forward
            curr = next_node           # move curr forward
        
        return prev