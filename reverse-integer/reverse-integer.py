class Solution:
    def reverse(self, x: int) -> int:
        """
        # Example x = 532
        res = 0
        
        while (x != 0):
            tail = x % 10; # Save the last digit to a var
            newResult = res * 10 + tail # save new result by moving current result digit left w/ * 10 and adding on the tail
            if((newResult - tail) // 10 != res):
                return 0
            res = newResult
            x = x // 10 # Remove last digit with integer division
            
        return res
        """
        
        negativeFlag = 1
        if x < 0:
            negativeFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)
            
        x = int(strx[::-1])
        
        return 0 if x > pow(2,31) else x * negativeFlag
        