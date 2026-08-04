class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMost, rightMost = 0, 0
        res = 0

        while l <= r:
            if leftMost < rightMost:
                leftMost = max(leftMost, height[l])
                res += leftMost - height[l]
                l += 1
            else:
                rightMost = max(rightMost, height[r])
                res += rightMost - height[r]
                r -= 1
        
        return res