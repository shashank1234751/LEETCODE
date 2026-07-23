class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        ans=[]
        start,end=0,0
        if k>0:
            start,end=1,k
        else:
            start,end=n-abs(k),n-1
        window=sum(code[start:end+1])
        for i in range(len(code)):
            ans.append(window)
            window -= code[start % n]
            start+=1
            end+=1
            window+=code[end%n]
        return ans

