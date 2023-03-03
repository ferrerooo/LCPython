from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque()
        index = 0
        while index < len(asteroids):
            
            a = asteroids[index]

            if not q:
                q.append(a)
                index += 1
                continue
            
            pre = q[-1]
            if pre < 0:
                q.append(a)
                index += 1
                continue

            if a > 0:
                q.append(a)
                index += 1
                continue
            
            if abs(pre) == abs(a):
                q.pop()
                index += 1
                continue
            
            if abs(pre) > abs(a):
                index += 1
                continue
            
            q.pop()
        
        return list(q)
            
