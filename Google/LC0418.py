from typing import List

class Solution0418:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        fullString = ' '.join(sentence)
        result = 0
        sentenceStart = 0

        for i in range(rows):
            availPositionStart = 0
            while (cols - availPositionStart) >= (len(fullString) - sentenceStart) :
                result = result + 1
                availPositionStart = availPositionStart + (len(fullString) - sentenceStart) + 1
                sentenceStart = 0
            if cols < availPositionStart:
                continue
            cursor = cols - availPositionStart + sentenceStart
            while fullString[cursor] != ' ':
                cursor = cursor - 1
            sentenceStart = cursor + 1
        
        return result

asolution = Solution0418()
sentence = ["f","p","a"]
rows = 8
cols = 7
result = asolution.wordsTyping(sentence, rows, cols)
print(f'The result is {result}')