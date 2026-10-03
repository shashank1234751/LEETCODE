class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini=float("inf")
        diff=0
        for n in prices:
            mini=min(n,mini)
            diff=max(n-mini,diff)
        return diff