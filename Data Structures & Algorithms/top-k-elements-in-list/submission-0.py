class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        sorted_items = sorted(hashmap.items(), key=lambda kv: kv[1])
        return [num for num, freq in sorted_items[-k:]]