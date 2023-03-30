# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        cur = [root]
        next = []
        result = []

        while len(cur) > 0:
            for node in cur:
                if node is None:
                    result.append(None)
                else:
                    result.append(node.val)
                    next.append(node.left)
                    next.append(node.right)

            cur = next
            next = []
        
        answer = ','.join(str(e) for e in result)
        print(f'serialize {answer}')
        return answer
                
                
        

    def deserialize(self, dataStr):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if len(dataStr) == 0:
            return None

        arr = dataStr.split(",")
        data = []
        for s in arr:
            if s != 'None':
                data.append(int(s))
            else:
                data.append(None)

        if data is None or len(data) == 0:
            return None
        

        print(f'deserialize {data}')

        root = TreeNode(data[0])

        cur = [root]
        next = []
        index = 1

        while len(cur) > 0:
            for node in cur:
                nextLeft = None
                if data[index] is not None:
                    nextLeft = TreeNode(data[index])
                node.left = nextLeft
                index += 1

                nextRight = None
                if data[index] is not None:
                    nextRight = TreeNode(data[index])
                node.right = nextRight
                index += 1

                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)

            cur = next
            next = []
        
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))