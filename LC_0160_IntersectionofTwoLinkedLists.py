# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = 0
        lenB = 0

        pa = headA
        pb = headB

        while pa:
            lenA += 1
            pa = pa.next
        
        while pb:
            lenB += 1
            pb = pb.next
        
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                headB = headB.next
        
        while headA and headB and headA is not headB:
            headA = headA.next
            headB = headB.next
        
        if headA is None:
            return None
        else:
            return headA
