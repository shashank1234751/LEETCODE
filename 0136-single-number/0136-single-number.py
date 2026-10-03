class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for key,item in freq.items():
            if item==1:
                return key