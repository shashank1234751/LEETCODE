class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum=prices[0]
        max_profit=0
        for price in prices:
            if minimum>price:
                minimum=price
            elif minimum<price:
                if price-minimum>max_profit:
                    max_profit=price-minimum
        return max_profit

            