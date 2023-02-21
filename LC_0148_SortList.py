# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = self.dfs(head, None)
        return head
    
    def dfs(self, head: ListNode, tail: ListNode) -> list[ListNode, ListNode]:
        
        if head is None or head is tail or head.next is tail:
            return head, tail

        fast = head
        slow = head

        while fast is not tail:
            fast = fast.next
            slow = slow.next
            if fast is not tail:
                fast = fast.next
        
        temp = slow.val
        slow.val = head.val
        head.val = temp

        dummy = ListNode()
        dummy.next = head
        toInsert = dummy
        pre = head
        cur = head.next

        while cur is not tail:
            if cur.val >= head.val:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur.next = toInsert.next
                toInsert.next = cur
                toInsert = toInsert.next
                cur = pre.next
     
        head1, tail1 = self.dfs(dummy.next, head)
        head2, tail2 = self.dfs(head.next, tail)

        tail1.next = head
        head.next = head2

        return head1, tail2

