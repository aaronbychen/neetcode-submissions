class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [-1,0,1,0,3]
        # [0,0,0,0,0]
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        res = []
        leftProd = [1]
        rightProd = [1]
        for i in range(len(nums)-1):
            leftProd.append(leftProd[i] * nums[i])
        for j in range(-1, -len(nums), -1):
            rightProd.insert(0, rightProd[j] * nums[j])
        for k in range(len(nums)):
            res.append(leftProd[k] * rightProd[k])
        return res