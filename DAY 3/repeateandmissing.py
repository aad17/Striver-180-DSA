'''
Litte Optimised:
Use extra space
T = O(N)
S = O(N)
'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        countarr = [0] * (n+1)
        a, b = 0, 0
        for i in range(n):
            countarr[A[i]] += 1
            if countarr[A[i]] > 1:
                a = A[i]
        
        for i in range(1, n+1):
            if countarr[i] == 0:
                b = i
                break

        return [a, b]

s = Solution()
print(s.repeatedNumber([1, 1]))