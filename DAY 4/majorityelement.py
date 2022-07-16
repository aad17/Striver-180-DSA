# Use of Hashmap
# TC = O(N)
# SC = O(N)

# import math

# class Solution:
#     def majorityElement(self, nums) -> int:
#         mydict = {}
#         for num in nums:
#             if num not in mydict:
#                 mydict[num] = 1
#             else:
#                 mydict[num] += 1
        
#         maj = math.ceil(len(nums)/2)
        
#         for key in mydict.keys():
#             if mydict[key] >= maj:
#                 return key


# Optimised
# Use of Moore's Voting Algorithm
# Step 1 -> Take 2 variables
#       a. Count
#       b. Element
# Step 2 -> Iterate through the array
# Step 3 -> If the next element is equal to previous element
#       a. Increment the count
#       b. else Decrement the count
# Step 4 -> If Count == 0
#       a. Change the element such that element = arr[i]
# Return the value stored inside the element

class Solution:
    def majorityElement(self, nums) -> int:
        count, element, size = 0, nums[0], len(nums)
        for i in range(size):
            if count == 0:
                element = nums[i]
            
            if element == nums[i]:
                count += 1
            else:
                count -= 1

        return element

s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))