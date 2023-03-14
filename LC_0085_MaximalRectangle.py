class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        pre = [0] * n
        answer = 0

        for row in range(m):
            cur = []
            for i in matrix[row]:
                cur.append(int(i))

            heights = []
            for col in range(n):
                if cur[col] == 0:
                    heights.append(0)
                else:
                    heights.append(1 + pre[col])
            local = self.largestRectangleArea(heights)
            print(f'answer:{answer}, local:{local}, row:{row}, pre:{pre}, cur:{cur}, heights:{heights}')
            answer = max(answer, local)

            pre = heights
        
        return answer

    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        answer = 0

        for i,v in enumerate(heights):
            if stack[-1] == -1 or v >= heights[stack[-1]]:
                stack.append(i)
                continue
            
            while len(stack) > 1:
                if v < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    #print(f'1-- i:{i}, v:{v}, h:{h}, w:{w}, stack[-1]:{stack[-1]}')
                    answer = max(answer, h*w)
                else:
                    break
            
            stack.append(i)
            
        while len(stack) > 1:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            answer = max(answer, h*w)
            #print(f'2-- h:{h}, w:{w}')
        
        return answer