# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        preleftPoint = dummy
        rightPoint = head

        for i in range(left-1):
            preleftPoint = preleftPoint.next
            rightPoint = rightPoint.next
        
        for i in range(right-left):
            rightPoint = rightPoint.next
        
        while preleftPoint.next is not rightPoint:
            temp = preleftPoint.next
            preleftPoint.next = temp.next
            temp.next = rightPoint.next
            rightPoint.next = temp
        
        return dummy.next
