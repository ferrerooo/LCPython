class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        p1 = 0
        p2 = m*n-1

        while p1 <= p2:
            
            mid = p1 + (p2-p1)//2

            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] > target:
                p2 = mid-1
            else:
                p1 = mid+1
        
        return False