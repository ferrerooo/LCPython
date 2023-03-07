from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = head = ListNode(0)
        queue = []
        count = 0
        for l in lists:
            if l is not None:
                count += 1
                heapq.heappush(queue, (l.val, count, l))
        while len(queue) > 0:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next
            if curr.next is not None:
                count += 1
                heapq.heappush(queue, (curr.next.val, count, curr.next))
        return head.next    