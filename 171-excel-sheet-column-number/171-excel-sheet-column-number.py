class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        pow = 1
        n = len(columnTitle)
        
        for i in range(n-1,-1,-1):
            ans = ans + (ord(columnTitle[i])-64)*pow
            pow = pow * 26
            
        return ans