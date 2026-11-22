# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None # Starts with an empty linked list
        curr = head # Start at the first node
        while curr:
            temp = curr.next # Saves the node that is after current
            curr.next = prev # flip the current point to point backwards
            prev = curr # Prev now takes current 
            curr = temp # Current is now the 'next' node 
        return prev # prev points to the first node of the fully reversed list.