from sortedcontainers import SortedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if groupSize == 0:
            return False

        if groupSize > len(hand) or len(hand)%groupSize != 0:
            return False
        
        c = collections.Counter(hand)
        sortedc = SortedDict(c)

        while len(sortedc.keys()) > 0:
            num = sortedc.keys()[0]
            for _ in range(groupSize):
                if num in sortedc:
                    sortedc[num] = sortedc[num] - 1
                    if sortedc[num] == 0:
                        del sortedc[num]
                    num += 1
                else:
                    return False
            

        return True