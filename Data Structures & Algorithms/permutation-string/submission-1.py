from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = defaultdict(int)
        window = defaultdict(int)
        for s in s1:
            need[s] += 1
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == need:
                return True

        return False