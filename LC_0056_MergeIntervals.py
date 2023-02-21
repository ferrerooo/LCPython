class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        answer = []

        for interval in intervals:

            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        
        return answer
