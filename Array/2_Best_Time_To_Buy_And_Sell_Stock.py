class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        # mini = nums[0]
        # cost, profit = 0, 0
        # for i in range(1, len(nums)):
        #     cost = nums[i] - mini
        #     profit = max(profit, cost)
        #     mini = min(mini, nums[i])
        # return profit

        buy_price = nums[0]
        profit = 0

        for p in nums[1:]:

            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        return profit