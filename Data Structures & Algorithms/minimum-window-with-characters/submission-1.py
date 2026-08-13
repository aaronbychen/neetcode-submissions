class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res = ""
        need = Counter(t)
        window = Counter()
        l = 0
        have = 0
        required = len(need)
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == required:
                if not res or r - l + 1 < len(res):
                    res = s[l:r+1]
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
        return res