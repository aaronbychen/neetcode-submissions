class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res_len = float('inf')
        res = ""
        need = Counter(t)
        window = Counter()
        have = 0
        need_count = len(need)
        l = 0
        for r in range(len(s)):
            r_char = s[r]
            window[r_char] += 1

            if r_char in need and need[r_char] == window[r_char]:
                have += 1
            while have == need_count:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]
                
                l_char = s[l]
                window[l_char] -= 1
                if l_char in need and window[l_char] < need[l_char]:
                    have -= 1
                l += 1
        return res