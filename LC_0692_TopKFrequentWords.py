class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # solution of sort
        '''
        cnt = Counter(words)
        return sorted(list(cnt.keys()), key=lambda x: (-cnt[x], x))[:k]
        '''
        #solution of heap
        cnt = Counter(words)
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
        