class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = []
        maxheap = []
        heapq.heapify(minheap)
        heapq.heapify(maxheap)
        p1 = 0
        p2 = 0
        answer = 0

        while p2 < len(nums):
            heapq.heappush(minheap, (nums[p2], p2))
            heapq.heappush(maxheap, (-1*nums[p2], p2))
            maxpair = maxheap[0]
            minpair = minheap[0]

            #print(maxheap)
            #print(minheap)

            #print(f'maxpair: {maxpair[0]}, {maxpair[1]}.  minpair: {minpair[0]}, {minpair[1]}')

            if (maxpair[0] * (-1) - minpair[0] <= limit):
                answer = max(answer, p2-p1+1)
                p2 += 1
                #print(maxpair[0] * (-1) - minpair[0])
                #print(answer)
                continue
            
            if maxpair[1] < minpair[1] :
                index = maxpair[1]
                while maxheap[0][1] <= index:
                    heapq.heappop(maxheap)
            else:
                index = minpair[1]
                while minheap[0][1] <= index:
                    heapq.heappop(minheap)
            
            p1 = index + 1
            p2 += 1
        
        return answer
            