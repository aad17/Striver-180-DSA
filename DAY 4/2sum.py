# Brute Force
# Iterate the array 2 times
# TC = O(N^2)
# SC = O(1)

# Optimised
# Use of Hash Map
# Store the number and its index in the hash map
# Calculate the difference between number and target
# If the difference is present in Hashmap
# Return the Number's index and Difference's index stored in hash map
# Else
# Store the number in hash map
class Solution:
    def twoSum(self, nums, target: int):
        mydict = {}
        for i, n in enumerate(nums):
            print(i, n)
            diff = target-n
            if diff in mydict:
                return [mydict[diff], i]
            
            mydict[n] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))