class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitString = s.rstrip().split(' ')
        print(splitString)
        return len(splitString[-1])