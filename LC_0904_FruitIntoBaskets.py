class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start = 0
        end = 0
        basket = {}
        result = 0
        
        while end < len(fruits):
            
            if fruits[end] in basket:
                basket[fruits[end]] += 1
                end += 1
                result = max(result, end - start)
                continue
                
            if len(basket) < 2:
                basket[fruits[end]] = 1
                result = max(result, end - start + 1)
            else:
                result = max(result, end - start)
                while len(basket) == 2:
                    basket[fruits[start]] -= 1
                    if basket[fruits[start]] == 0:
                        basket.pop(fruits[start])
                    start += 1
                basket[fruits[end]] = 1
            
            end += 1
        
        return result
        
            