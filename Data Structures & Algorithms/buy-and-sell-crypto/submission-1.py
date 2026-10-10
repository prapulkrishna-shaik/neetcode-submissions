class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff = prices[j]-prices[i]
        #         mini = max(mini,diff)
        # return mini

        #optimization prefix min and max from the end

        maxi = float('-inf')
        ans = 0
        
        for i in range(len(prices)):
            mini = min(mini,prices[i])
          
            ans = max(ans,(prices[i]-mini))
        return ans 








