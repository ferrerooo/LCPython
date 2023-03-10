class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxheap = []
        minheap = []
        heapq.heapify(maxheap)
        heapq.heapify(minheap)
        maxsize = k//2 + k%2
        minsize = k//2
        
        for i in range(k):
            heapq.heappush(minheap, (nums[i], i))
        
        while len(maxheap) != maxsize:
            (val, idx) = heapq.heappop(minheap)
            heapq.heappush(maxheap, (-1 * val, idx) )
        
        answer = []

        p1 = 0
        p2 = k-1

        while p2 < len(nums):

            p1 += 1
            p2 += 1

            if k%2 == 1:
                answer.append(maxheap[0][0] * (-1))
            else:
                answer.append((maxheap[0][0] * (-1) + minheap[0][0])/2)

            if p2 == len(nums):
                break

            toremoveval = nums[p1-1]
            toaddval = nums[p2]

            if toremoveval <= (maxheap[0][0] * -1):
                maxsize -= 1
            else:
                minsize -= 1


            while len(maxheap) > 0 and maxheap[0][1] < p1:
                heapq.heappop(maxheap)
            
            while len(minheap) > 0 and minheap[0][1] < p1:
                heapq.heappop(minheap)


            
            if len(maxheap) > 0 and toaddval <= (maxheap[0][0] * -1):
                heapq.heappush(maxheap, (toaddval * -1, p2))
                maxsize += 1
            else:
                heapq.heappush(minheap, (toaddval, p2))
                minsize += 1

            while maxsize < (k//2 + k%2):
                (val, idx) = heapq.heappop(minheap)
                if idx < p1:
                    continue
                minsize -= 1
                heapq.heappush(maxheap, (-1 * val, idx))
                maxsize += 1
            
            while maxsize > (k//2 + k%2):
                (val, idx) = heapq.heappop(maxheap)
                if idx < p1:
                    continue
                maxsize -= 1
                heapq.heappush(minheap, (-1 * val, idx))
                minsize += 1

        return answer