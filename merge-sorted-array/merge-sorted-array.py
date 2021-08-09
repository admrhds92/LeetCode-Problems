class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            #If the last element of 1 is greater than 2... put the last element of 1 to the end of the extended array
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
            #Else put the last element of 2 to the end of the extended array 
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            #If there is any left in array2 they go in place into array1
            nums1[n-1] = nums2[n-1]
            n -= 1