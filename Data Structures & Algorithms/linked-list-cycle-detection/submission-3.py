# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Use slow and fast pointers to detect a cycle in the linked list

        slow moves one node at a time
        fast moves two nodes at a time

        The idea is:
        - if there is no cycle, fast will eventually reach the end of the list
        - if there is a cycle, fast will eventually catch up to slow inside the cycle

        We continue while fast and fast.next exist
        - fast must exist so we can safely access fast.next
        - fast.next must exist so we can safely move fast two steps forward

        If slow and fast ever point to the same node, there must be a cycle

        If the loop ends, fast reached the end of the list, so there is no cycle

        TC: O(n), where n is the number of nodes
        - slow and fast move through the list until either a cycle is found or the end is reached

        SC: O(1)
        - we only use two pointer variables
        '''

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False