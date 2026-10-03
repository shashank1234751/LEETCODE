class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        pre = 1
        for i in range(n):
            prefix[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = suf
            suf *= nums[i]

        for i in range(n):
            prefix[i] *= suffix[i]

        return prefix