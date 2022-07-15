'''
Use Count Sort
T = O(N)
S = O(N)
'''
class Solution:
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        countlist = [0] * (n+1)

        for i in range(n):
            countlist[nums[i]] += 1
            if countlist[nums[i]] > 1:
                return nums[i]

s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))