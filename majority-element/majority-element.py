class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        
        for num in nums:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] += 1
          
        
        return max(numCount, key=numCount.get)
        #allValues = numCount.values()
        #maxValue = max(allValues)
        #print(numCount)
        
        """for num in numCount:
            if numCount.get(num) == maxValue:
                return num"""
            
        