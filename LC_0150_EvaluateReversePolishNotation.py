class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                c = 0
                if s == '+':
                    c = a+b
                if s == '-':
                    c = a-b
                if s == '*':
                    c = a*b
                if s == '/':
                    c = a//b
                    if c < 0 and abs(a)%abs(b) != 0:
                        c += 1
                stack.append(c)
            else:
                stack.append(int(s))
            
            #print(stack)
        
        return stack[-1]