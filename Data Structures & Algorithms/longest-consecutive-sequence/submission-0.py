class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        print(hashset)
        for n in hashset:
            length = 0
            if (n - 1) not in hashset:
                target = n
                while target in hashset:
                    length += 1
                    target += 1
                if length > res:
                    res = length
        return res