class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        result = 0
        minHeap = []
        heapify(minHeap)
        
        for index, val in enumerate(heights):
            
            if index == 0:
                continue
            
            if heights[index] <= heights[index-1]:
                result = index
                continue
            
            gap = heights[index] - heights[index-1]
            
            if ladders > 0:
                ladders = ladders - 1
                heappush(minHeap, gap)
                result = index
                continue
            
            if len(minHeap) == 0 or minHeap[0] >= gap:
                if bricks >= gap:
                    bricks = bricks - gap
                    result = index
                    continue
                else:
                    result = index - 1
                    break;
            else:
                if bricks >= minHeap[0]:
                    bricks = bricks - minHeap[0]
                    heappop(minHeap)
                    heappush(minHeap, gap)
                    result = index
                    continue
                else:
                    result = index - 1
                    break
        
        return result
                
        