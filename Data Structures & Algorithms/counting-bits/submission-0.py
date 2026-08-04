class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
        # 1d: 0, 1,
        # 2d: 1, 2,
        # 3d: 1, 2, 2, 3
        # 4d: 1, 2, 2, 3, 2, 3, 3, 4
        # 5d: 16