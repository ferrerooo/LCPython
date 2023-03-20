# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        p1 = 0
        p2 = n - 1

        while p1 < p2:
            if knows(p1, p2):
                p1 += 1
            else:
                p2 -= 1
        
        answer = p1

        for i in range(n):
            if i == p1:
                continue
            if not knows(i, p1) or knows(p1, i):
                answer = -1
                break
        
        return answer