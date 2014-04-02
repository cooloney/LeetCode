class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        # DP lists
        dl = [0] * len(prices) # max val in prices[0:i]
        dr = [0] * len(prices) # max val in prices[i+1:len(prices)-1]
        
        # Init DP start case
        dl[0] = 0
        dr[len(prices)-1] = 0
        
        # Build DP lists
        left_min = prices[0]
        for i in range(1, len(prices)):
            dl[i] = max(dl[i-1], prices[i]-left_min)
            left_min = min(left_min, prices[i])
	    print dl, left_min

        right_max = prices[len(prices)-1]
        for j in range(len(prices)-2, -1, -1):
            dr[j] = max(dr[j+1], right_max - prices[j])
            right_max = max(right_max, prices[j])
	    print dr, right_max
        
        # Get the max dl[i]+dr[i]
        res = 0
        for i in range(len(prices)):
            res = max(res, dl[i]+dr[i])
        
        return res

if __name__ == "__main__":
    prices = [1, 2, 4]
    print prices
    s = Solution()
    print s.maxProfit(prices)


