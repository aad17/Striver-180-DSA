'''
Use of KADANE'S ALGORITHM
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        # Initialise maximum sum and current sum as 0
        currSum = 0
        maxSum = 0

        # Iterate through array
        for num in nums:
            # IF CURRENT SUM < 0 THEN MAKE CURRENT SUM = 0
            if currSum < 0:
                currSum = 0

            # Add the current sum with the number
            currSum += num

            # Find the maximum of current sum and maximum sum
            maxSum = max(maxSum, currSum)

        return maxSum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))