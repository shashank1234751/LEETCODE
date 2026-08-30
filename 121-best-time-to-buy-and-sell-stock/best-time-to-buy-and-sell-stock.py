class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=0
        mini=float("inf")
        for n in prices:
            diff=max(diff,n-mini)
            mini=min(mini,n)
        return diff