class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for num in range(1, (n+1)):
            div_5 = (num % 5 == 0)
            div_3 = (num % 3 == 0)
            
            if div_5 and div_3:
                ans.append("FizzBuzz")
            elif div_5:
                ans.append("Buzz")
            elif div_3:
                ans.append("Fizz")
            else:
                ans.append(str(num))
                
        return ans
    
