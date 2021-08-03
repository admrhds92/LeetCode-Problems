class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest = 0
      
        for i in range(len(accounts)):
            current = 0
            for j in range(len(accounts[i])):
                current += accounts[i][j]
                print(current)
                
            if current > wealthiest:
                wealthiest = current
                
        return wealthiest 