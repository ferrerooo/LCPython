from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        q1 = self.parse(s)
        #print(q1)
        q2 = deque()
        while q1:
            if q1[0] not in ('*', '/'):
                q2.append(q1.popleft())
            else:
                a = q2.pop()
                op = q1.popleft()
                b = q1.popleft()
                c = 0
                if op == '*':
                    c = int(a) * int(b)
                else:
                    c = int(a) // int(b)
                q2.append(str(c))
        #print(q2)
        while q2 and len(q2) > 1:
            a = q2.popleft()
            op = q2.popleft()
            b = q2.popleft()
            c = 0
            if op == '+':
                c = int(a) + int(b)
            else:
                c = int(a) - int(b)
            q2.appendleft(str(c))

        return int(q2[0])
    
    def parse(self, s: str):
        arr = deque()
        p = 0
        while p < len(s):
            if s[p] in ('+', '-', '*', '/'):
                arr.append(s[p])
            elif s[p] == ' ':
                pass
            else:
                p1 = p
                while p1 < len(s) and s[p1] not in ('+', '-', '*', '/', ' '):
                    p1 += 1
                arr.append(s[p:p1])
                p = p1 - 1
            
            p += 1
        return arr
