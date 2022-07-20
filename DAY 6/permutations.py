class Solution:
    def permute(self, nums):
        ans = []
        def recurse(nums, ds, freq):
            if len(ds) == len(nums):
                ans.append(ds.copy())
                return

            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    ds.append(nums[i])
                    recurse(nums, ds, freq)
                    ds.pop()
                    freq[i] = False
        
        freq = [False] * len(nums)
        recurse(nums, [], freq)
        return ans

s = Solution()
print(s.permute([1, 2, 3]))