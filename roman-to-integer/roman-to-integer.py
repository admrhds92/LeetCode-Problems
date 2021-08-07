class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        ans = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]: # If the symbol before the next is less then we subtract the current symbol
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]] 
        return ans + roman[s[-1]] # Always add the last letter