import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in heapq.nlargest(k, nums):
            print(i)
        
        return heapq.nlargest(k, nums)[-1]