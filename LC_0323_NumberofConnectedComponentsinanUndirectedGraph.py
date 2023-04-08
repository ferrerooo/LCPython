class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        nodemap = {}
        for edge in edges:

            a = edge[0]
            b = edge[1]
            if a not in nodemap:
                nodemap[a] = []
            if b not in nodemap:
                nodemap[b] = []
            nodemap[a].append(b)
            nodemap[b].append(a)

        answer = 0
        visited = set()

        for i in range(n):
            if i not in nodemap:
                answer += 1

        for key in nodemap:

            if key in visited:
                continue

            answer += 1

            q = collections.deque()
            q.append(key)

            while q:
                cur = q.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for neighbor in nodemap[cur]:
                    if neighbor not in visited:
                        q.append(neighbor)
        
        return answer
