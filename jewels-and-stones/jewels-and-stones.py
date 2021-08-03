class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        #for i in stones:
            #if i in jewels:
                #count += 1
                
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
        
        return count