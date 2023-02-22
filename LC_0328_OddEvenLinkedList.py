# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None or head.next.next is None:
            return head
        
        dummy1 = ListNode()
        dummy2 = ListNode()
        cur1 = dummy1
        cur2 = dummy2

        pointer = head

        while pointer:
            cur1.next = pointer
            cur1 = cur1.next
            pointer = pointer.next
            cur2.next = pointer
            cur2 = cur2.next
            if pointer:
                pointer = pointer.next
        
        cur1.next = dummy2.next
        return dummy1.next

