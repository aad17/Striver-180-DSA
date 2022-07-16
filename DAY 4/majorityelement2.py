# Use of Hashmap
# TC = O(N)
# SC = O(N)

# import math

# class Solution:
#     def majorityElement(self, nums):
#         mydict = {}
#         for num in nums:
#             if num not in mydict:
#                 mydict[num] = 1
#             else:
#                 mydict[num] += 1
        
#         maj = int(len(nums)/3)
#         op = []
#         for key in mydict.keys():
#             if mydict[key] > maj:
#                 op.append(key)
                
#         return op

# Optimised
# Use of Moore's Voting Algorithm
# Step 1 -> Take 4 variables
#       a. Count1
#       b. Element1
#       c. Count2
#       d. Element2
# Step 2 -> Iterate through the array
# Step 3 -> If the next element1 or element2 is equal to previous element
#       a. Increment the count1 or count2
#       b. else Decrement the count1 or count2
# Step 4 -> If Count1 == 0
#       a. Change the element such that element1 = arr[i]
# Step 5 -> If Count2 == 0
#       b. Change the element such that element2 = arr[i]
# But they cannot guarentee the > n/3 times
# Hence count the occurences of element1 and element2 in the array
# Return the value stored inside the element1 and element2 if > n/3

import math
class Solution:
    def majorityElement(self, nums):
        num1, num2, cnt1, cnt2, n = -1, -1, 0, 0, len(nums)
        for i in range(n):
            if nums[i] == num1:
                cnt1 += 1
            elif nums[i] == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = nums[i]
                cnt1 += 1
            elif cnt2 == 0:
                num2 = nums[i]
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans = []
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if num1 == nums[i]:
                cnt1 += 1
            elif num2 == nums[i]:
                cnt2 += 1

        if cnt1 > math.floor(n/3):
            ans.append(num1)
        if cnt2 > math.floor(n/3):
            ans.append(num2)

        return ans

s = Solution()
print(s.majorityElement([2, 2, 1, 3]))