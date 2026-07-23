class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        final=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                final.append(nums1[i])
                i+=1
            else:
                final.append(nums2[j])
                j+=1
        while i<len(nums1):
            final.append(nums1[i])
            i+=1
        while j<len(nums2):
            final.append(nums2[j])
            j+=1
        n=len(final)
        if n%2==1:
            return final[n // 2]
        else:
            return (final[n // 2 - 1] + final[n // 2]) / 2.0