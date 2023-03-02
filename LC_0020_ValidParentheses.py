class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        bracketMap = {')':'(', ']':'[', '}':'{'}

        while index < len(s):
            if s[index] in ('(', '[', '{'):
                stack.append(s[index])
            else:
                if not stack or stack[-1] != bracketMap[s[index]]:
                    return False
                else:
                    stack.pop()
            index += 1
        
        if stack:
            return False
        else:
            return True