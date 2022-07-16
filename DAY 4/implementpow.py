# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             res = 1/x
#             while n < -1:
#                 res *= 1/x
#                 n += 1
#             return res
        
#         elif n > 0:
#             res = x
#             while n > 1:
#                 res *= x
#                 n -= 1
#             return res
        
#         elif n == 0:
#             return 1

# TC = O(log N)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n
        if nn < 0:
            nn = -1 * nn
        while nn > 0:
            if nn % 2 == 1:
                ans = ans * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn / 2

        if n < 0:
            ans = 1.0/ans
        
        return ans

s = Solution()
print(s.myPow(2.00000, -4))