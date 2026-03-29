class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = 0
        maxp = 1
        profit = 0
        while (maxp < len(prices)):
            print(minp, prices[minp], maxp, prices[maxp])
            profit = max(profit, (prices[maxp]- prices[minp]))
            if (prices[minp] > prices[maxp]):
                minp = maxp
            maxp += 1
            print(f'Profit: {profit}')
        return profit