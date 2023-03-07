from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l)) # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        while not q.empty():
            val, node = q.get()
            point.next = node
            nextNode = node.next
            point = point.next
            point.next = None
            if nextNode:
                q.put((nextNode.val, nextNode))
        
        return head.next
        