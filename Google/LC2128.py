class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:

        row0 = grid[0]
        row0_reverse = [1 - val for val in grid[0]]
        for i in range(1, len(grid)):
            if row0 != grid[i] and row0_reverse != grid[i]:
                return False
        return True