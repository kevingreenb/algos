class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        prev = None
        while max_heap or prev:
            if not max_heap and prev:
                return ""
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            freq += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if freq < 0:
                prev = (freq, char)
        return "".join(res)