# Use of Recursion
# Take/Not Take the element
# Key point is we can pick the single element from the giver array
# ANY number of times
# So, for doing it
# While selecting the element we do not have to move forward the array
# And while not selecting the element we have to move forward

class Solution:
    def combinationSum(self, candidates, target: int):
        n = len(candidates)
        ans = []
        def helper(candidates, target, ds, idx, n):
            if idx >= n:
                if target == 0:
                    ans.append(ds.copy())
                return
            
            # Selecting the element
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                # While selecting we have to reduce the target
                helper(candidates, target - candidates[idx], ds, idx, n)
                ds.pop()
            
            # Not selecting the element
            # We have to move forward the array
            helper(candidates, target, ds, idx+1, n)
        
        helper(candidates, target, [], 0, n)
        return ans

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))