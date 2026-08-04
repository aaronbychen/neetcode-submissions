class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal_idx = n - 1
        start_idx = n - 2
        for i in range(start_idx, -1, -1):
            if nums[i] >= (goal_idx - i):
                goal_idx = i
            else:
                continue
        return True if goal_idx == 0 else False