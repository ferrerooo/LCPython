# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        reversedHead = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = reversedHead
            reversedHead = cur
            cur = temp
        
        return reversedHead
