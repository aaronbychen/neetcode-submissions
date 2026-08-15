class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            if r - l + 1 == k:
                if dq and dq[0] < l:
                    dq.popleft()
                res.append(nums[dq[0]])
                l += 1
        return res
