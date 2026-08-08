class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tem_suf=1
        tem_pre=1
        sufix=[]
        prefix=[]
        result=[]
        for i in range(len(nums)):
            prefix.append(tem_pre)
            tem_pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            sufix.insert(0,tem_suf)
            tem_suf*=nums[i]
        for i in range(len(prefix)):
            ans=prefix[i]*sufix[i]
            result.append(ans)
        return result
    