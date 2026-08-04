class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        pivot = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[pivot]:
                    pivot = l
                break
            
            m = l + (r - l) // 2
            if nums[m] < nums[pivot]:
                pivot = m
            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        
                left = 0
        # 注意
        if pivot == 0:
            left, right = 0, len(nums) - 1
        elif nums[0] <= target and nums[pivot - 1] >= target:
            left, right = 0, pivot - 1
        elif nums[pivot] <= target and nums[len(nums) - 1] >= target:
            left, right = pivot, len(nums) - 1
        else:
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 注意
                left = mid + 1
            elif nums[mid] > target:
                # 注意
                right = mid - 1
        return res