class Solution:
    def maxProfit(self, prices) -> int:
        # Take 2 pointers left and right
        l, r = 0, 1
        # Initilise maximum profit to be equal to 0
        maxProfit = 0

        # Iterate while right is less than length of the array
        while r < len(prices):
            # If price at left index is less than price at right index
            # Then Profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

            # If not a profitable transaction then make left index = right index
            else:
                l = r
            
            # Increment right index
            r += 1

        return maxProfit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))