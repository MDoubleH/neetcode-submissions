# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use a dummy node to make building the merged linked list easier

        dummy keeps track of the start of the merged list
        - we return dummy.next at the end because dummy itself is just a placeholder

        curr keeps track of where we are currently adding nodes in the merged list

        Since both lists are already sorted:
        - compare the current value of list1 and list2
        - attach the smaller node to curr.next
        - move the list pointer forward for whichever node we used
        - move curr forward so we can attach the next node

        Keep doing this while both lists still have nodes

        Once one list becomes empty:
        - the remaining nodes in the other list are already sorted
        - so we can attach the rest directly to curr.next

        TC: O(n + m), where n is the length of list1 and m is the length of list2
        - we visit each node once

        SC: O(1)
        - we are reusing the existing nodes and only using dummy/curr pointers
        - ignoring the output list, no extra data structure is created
        '''
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next