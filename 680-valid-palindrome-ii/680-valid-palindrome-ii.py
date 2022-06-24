def check(s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start+=1
            end -=1
        
        return True
            
class Solution:
  
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        
        while start <= end:
            if s[start] != s[end]:
                # 2 cases. Delete start or delete end then check the remaining inner string isPalindrome
                if check(s, start+1, end) or check(s, start, end-1):
                    return True
                else:
                    return False
            else:
                start += 1
                end -= 1
                
        return True #String is already a palindrome
            