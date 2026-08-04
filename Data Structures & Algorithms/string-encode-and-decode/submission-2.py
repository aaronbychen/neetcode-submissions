class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "EMPTY_LIST_MARKER"
        res=""
        for i in range(len(strs)-1):
            res+= strs[i]+"é"
        res+=strs[len(strs)-1]
        return res

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST_MARKER":
            return []
        return s.split("é")
