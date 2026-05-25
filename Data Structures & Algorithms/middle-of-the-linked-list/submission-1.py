# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use slow and fast pointers to find the middle of the linked list

        slow moves one node at a time
        fast moves two nodes at a time

        The idea is:
        - by the time fast reaches the end of the list
        - slow will be halfway through the list
        - so slow will be pointing at the middle node

        The loop continues while fast and fast.next both exist
        - fast must exist so we can safely access fast.next
        - fast.next must exist so we can safely move fast two steps forward

        If the list has an odd number of nodes:
        - slow lands exactly on the middle node

        If the list has an even number of nodes:
        - slow lands on the second middle node
        - this matches what the problem asks for

        TC: O(n), where n is the number of nodes
        - fast moves through the list once

        SC: O(1)
        - we only use two pointer variables
        '''

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        return slow