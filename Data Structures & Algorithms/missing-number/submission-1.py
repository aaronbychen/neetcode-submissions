class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        n = len(nums)
        for num in nums:
            hashmap[num] += 1
        for i in range(n + 1):
            if i not in hashmap.keys():
                return i