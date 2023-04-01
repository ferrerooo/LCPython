class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()
        visited.add(beginWord)
        cur = collections.deque()
        next = collections.deque()
        cur.append(beginWord)
        L = len(beginWord)
        step = 1
        
        while cur:
            for w in cur:
                for i in range(L):
                    for letter in range(ord('a'), ord('z')+1):
                        newWord = w[:i] + chr(letter) + w[i+1:]
                        if newWord in wordSet and str(chr(letter)) != w[i] and newWord not in visited:
                            next.append(newWord)
                            visited.add(newWord)
                            if newWord == endWord:
                                return step+1
            
            step += 1
            cur = next
            next = collections.deque()
        
        return 0

                    
