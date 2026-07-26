class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        freq={}

        for n in nums:
            freq[n]=freq.get(n,0)+1
        sort = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        for num,keys in sort[:k]:
            ans.append(num)
        return ans


        