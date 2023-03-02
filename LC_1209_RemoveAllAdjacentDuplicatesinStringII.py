class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = []
        index = 0
        while index < len(s):
            if not q or q[-1][0] != s[index]:
                q.append([s[index], 1])
            else:
                q[-1][1] += 1
                if q[-1][1] == k:
                    q.pop()
            index += 1
        
        answer = ''
        for pair in q:
            for i in range(pair[1]):
                answer += pair[0]
        
        return answer
