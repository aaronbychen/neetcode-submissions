class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += 1 if n % 2 == 1 else 0
            n = n >> 1
        return res