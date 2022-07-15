'''
Use GAP Method
Step 1 -> Take GAP = math.ceil((m + n)/2)
Step 2 -> i = 0, j = GAP
Step 3 -> Iterate while GAP > 0
Step 4 -> if i < j then swap the elements
Step 5 -> Decrease the GAP such that GAP = math.ceil(GAP/2)
'''
import math
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        gap = math.ceil(m+n/2)
        
        i, j =  0, 0
        while gap > 0:
            while j < (m + n):
                if j < n and nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
                elif j >= n and i < n and nums1[i] > nums2[j-n]:
                    nums1[i], nums2[j-n] = nums2[j-n], nums1[i]
                elif j >= n and i >= n and nums2[i-n] > nums2[j-n]:
                    nums2[i-n], nums2[j-n] = nums2[j-n], nums2[i-n]
                i += 1
                j += 1
            
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap / 2)

        k = i    
        for i in range(n):
            nums1[k] = nums2[i]
            k += 1
            
        return nums1

s = Solution()
print(s.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5))
