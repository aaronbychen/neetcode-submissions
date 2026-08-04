from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1
            maxChar = max(hashmap, key=hashmap.get)
            maxFreq = hashmap[maxChar]
            while (r - l + 1) - maxFreq > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

