# Little Optimised Method
# Time Complexity = O(N)
# Space Complexity = O(N)
# Use of Count Sort Approach
# class Solution:
#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # Brute force
#         count_arr = [0] * 3
#         for num in nums:
#             count_arr[num] += 1
            
#         i = 0
#         k = 0
#         while count_arr[i] > 0:
#             nums[k] = 0
#             k += 1
#             count_arr[i] -= 1
        
#         i += 1
        
#         while count_arr[i] > 0:
#             nums[k] = 1
#             k += 1
#             count_arr[i] -= 1
        
#         i += 1
        
#         while count_arr[i] > 0:
#             nums[k] = 2
#             k += 1
#             count_arr[i] -= 1
            
#         print(count_arr)
#         return nums


# Optimised
# Dutch FLag Algo
# Take 3 pointers
#   1. Low pointing to first index
#   2. Mid pointing to first index
#   3. High pointing to last index

# 3 conditions
#   1. If mid == 0
#       a. Swap(mid, low)
#       b. mid += 1
#       c. low += 1
#   2. If mid ==  1
#       a. mid += 1
#   3. If mid == 2
#       a. Swap(mid, high)
#       b. high -= 1

# Time Complexity = O(N)
# Space Complexity = O(1)

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        # i = 0
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums

s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
