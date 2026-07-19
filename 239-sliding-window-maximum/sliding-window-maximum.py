import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        heap = []
        ans = []

        for i in range(len(nums)):

            # Push current element
            heapq.heappush(heap, (-nums[i], i))

            # Remove elements outside the window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # Window is ready
            if i >= k - 1:
                ans.append(-heap[0][0])

        return ans
        