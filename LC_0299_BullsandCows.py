class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        nonBullDic = {}
        nonBullList = []
        for i, cs in enumerate(secret):
            cg = guess[i]
            if cs == cg:
                bulls += 1
            else:
                nonBullList.append(cg)
                if cs not in nonBullDic:
                    nonBullDic[cs] = 0
                nonBullDic[cs] += 1
        
        for cs in nonBullList:
            if cs in nonBullDic:
                cows += 1
                nonBullDic[cs] -= 1
                if nonBullDic[cs] == 0:
                    del nonBullDic[cs]
        
        return str(bulls)+ 'A' + str(cows) + 'B'