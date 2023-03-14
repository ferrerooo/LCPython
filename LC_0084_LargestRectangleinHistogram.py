class Solution:
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
                