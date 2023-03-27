# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedDict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        sd = SortedDict()
        #self.dfs(root, sd, 0)
        cur = []
        next = []
        cur.append((root, 0))

        while len(cur) > 0:
            for pair in cur:
                node = pair[0]
                column = pair[1]
                if column not in sd:
                    sd[column] = []
                sd[column].append(node.val)
                if node.left is not None:
                    next.append((node.left, column-1))
                if node.right is not None:
                    next.append((node.right, column+1))
            
            cur = next
            next = []

        answer = []

        for col in sd.values():
            answer.append(col)
        
        return answer
    
    def dfs(self, node, sd, column):
        if column not in sd:
            sd[column] = []
        sd[column].append(node.val)
        if node.left is not None:
            self.dfs(node.left, sd, column-1)
        if node.right is not None:
            self.dfs(node.right, sd, column+1)