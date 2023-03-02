class Solution:
    def removeDuplicates(self, s: str) -> str:
        q = []
        index = 0
        while index < len(s):
            if not q or q[-1] != s[index]:
                q.append(s[index])
            else:
                q.pop()
            index += 1
        
        return ''.join(q)