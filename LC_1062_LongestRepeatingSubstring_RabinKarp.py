class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 1
        p2 = n-1
        answer = 0

        nums = []

        while p1 <= p2:
            mid = (p1+p2)//2
            if self.search(mid, s) != -1:
                p1 = mid+1
                answer = mid
            else:
                p2 = mid-1
        
        return answer
    
    def search(self, mid:int, s:str) -> int:
        base = 26
        modulus = pow(2, 24)
        hash = 0

        for i in range(mid):
            hash = (hash * base % modulus + (ord(s[i])-ord('a'))) % modulus
        
        seen = {}
        seen[hash] = set()
        seen[hash].add(0)

        #print(f'substr:{s[0:mid]}, hash:{hash}, seen:{seen.keys()}, mid:{mid}')

        maxHashBase = 1
        for i in range(1, mid+1):
            maxHashBase = (maxHashBase * base) % modulus
        
        for i in range(1, len(s)-mid+1):
            hash = (hash*base - (ord(s[i-1])-ord('a')) * maxHashBase % modulus + modulus) % modulus
            hash = (hash + (ord(s[i+mid-1])-ord('a'))) % modulus
            #print(f'substr:{s[i:i+mid]}, hash:{hash}, seen:{seen.keys()}, mid:{mid}')
            if hash in seen:
                seenSet = seen[hash]
                #print(f'seen hash:{hash}')
                for h in seenSet:
                    if self.isSame(s, h, i, mid):
                        #print(f's:{s}, h:{h}, i:{i}, mid:{mid}')
                        return True
                
                seen[hash].add(i)
            else:
                #print(f'NOT seen hash:{hash}, seenSize:{len(seen)}, mid:{mid}')
                seen[hash] = set()
                seen[hash].add(i)

        return -1

    def isSame(self, s:str, start1:int, start2:int, len:int) -> bool:
        return s[start1:start1+len] == s[start2:start2+len]