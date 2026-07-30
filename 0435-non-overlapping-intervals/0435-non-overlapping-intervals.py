class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last=intervals[0][1]
        ans=0
        for i in range(1,len(intervals)):
            if last>intervals[i][0]:
                ans+=1
                last = min(last, intervals[i][1])
            else:
                last=intervals[i][1]
        return ans
