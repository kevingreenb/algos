class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord("a")] += 1
            g[tuple(count)].append(word)
        
        return list(g.values())
        