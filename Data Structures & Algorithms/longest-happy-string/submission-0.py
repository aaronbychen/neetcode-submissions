import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []

        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-2] == res[-1] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2 += 1
                res += char2
                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, char2))
            count += 1
            res += char
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        return res