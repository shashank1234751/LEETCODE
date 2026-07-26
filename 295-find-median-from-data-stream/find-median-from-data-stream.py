class MedianFinder:

    def __init__(self):
        self.ans=[]
        

    def addNum(self, num: int) -> None:
        self.ans.append(num)

    def findMedian(self) -> float:
        self.ans.sort()
        n=len(self.ans)//2
        if len(self.ans)%2==0:
            return (self.ans[n-1]+self.ans[n])/2
        return self.ans[n]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()