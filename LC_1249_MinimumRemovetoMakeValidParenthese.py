class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                pass
            else:
                if c == '(':
                    stack.append(i)
                else:
                    if not stack or s[stack[-1]] == ')':
                        stack.append(i)
                    else:
                        stack.pop()
        
        removeSet = set(stack)
        stringBuilder = []
        for i, c in enumerate(s):
            if i not in removeSet:
                stringBuilder.append(c)
        
        return ''.join(stringBuilder)
        