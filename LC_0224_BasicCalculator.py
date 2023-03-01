class Solution:
    def calculate(self, s: str) -> int:
        arr = self.parse(s)
        print(arr)
        q = []
        index = 0
        while index < len(arr):
            if arr[index] != ')':
                q.append(arr[index])
            else:
                localQ = []
                while q[-1] != '(':
                    localQ.append(q.pop())
                q.pop()
                localQ.reverse()
                #print(localQ)
                localResult = self.cal(localQ)
                q.append(str(localResult))
            index += 1
        
        if q[0] == '-':
            q.insert(0, '0')
        return self.cal(q)
    
    def cal(self, arr) -> int:
        if arr[0] == '-':
            arr.insert(0, '0')
        while len(arr) > 1:
            a = int(arr.pop(0))
            op = arr.pop(0)
            b = int(arr.pop(0))
            c = 0
            if op == '+':
                c = a+b
            else:
                c = a-b
            arr.insert(0,c)
        return int(arr[0])

    def parse(self, s: str) -> List[str]:
        p = 0
        arr = []
        while p < len(s):
            if s[p] == '+':
                arr.append('+')
                p += 1
            elif s[p] == '-':
                arr.append('-')
                p += 1
            elif s[p] == '(':
                arr.append('(')
                p += 1
            elif s[p] == ')':
                arr.append(')')
                p += 1
            elif s[p] == ' ':
                p += 1
                pass
            else:
                p1 = p
                while p1 < len(s) and s[p1] not in ('+', '-', '(', ')', ' '):
                    p1 += 1
                arr.append(s[p:p1])
                p = p1
        return arr
