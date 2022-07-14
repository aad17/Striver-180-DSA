class Solution:
    def merge(self, intervals) -> None:
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = []
        tempInterval = intervals[0]
        for it in intervals:
            if it[0] <= tempInterval[1]:
                tempInterval[1] = max(tempInterval[1], it[1])
            else:
                ans.append(tempInterval)
                tempInterval = it

        ans.append(tempInterval)
        return ans

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))