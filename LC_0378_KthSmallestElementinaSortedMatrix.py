class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        p1 = matrix[0][0]
        p2 = matrix[n-1][n-1]
        answer = 0
        while p1 <= p2:
            mid = (p1+p2)//2
            smaller, equal, larger = self.binarySearch(matrix, mid)
            if smaller >= k:
                p2 = mid - 1
                continue

            if smaller + equal < k:
                p1 = mid + 1
                continue
            
            if smaller + equal >= k:
                answer = mid
                break

        return answer
    
    def binarySearch(self, matrix, val):
        smaller = 0
        equal = 0
        larger = 0
        n = len(matrix)

        row = n-1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] < val:
                smaller += (row+1)
                col += 1
            elif matrix[row][col] > val:
                larger += (n-col)
                row -= 1
            else:
                for c in range(col, n):
                    if matrix[row][c] == val:
                        equal += 1
                    else:
                        larger += (n-c)
                        break
                row -= 1
        
        return smaller, equal, larger
