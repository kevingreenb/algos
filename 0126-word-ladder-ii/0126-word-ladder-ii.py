class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        if beginWord not in wordList:
            wordList.add(beginWord)
        

        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)
        
        dist = {beginWord: 0}
        parent = defaultdict(list)
        q = deque([beginWord])
        found = False
        
        while q and not found:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                curr_dist = dist[curr]
                
                if curr == endWord:
                    found = True
                    continue
                
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for neighbor in g[pattern]:
                        if neighbor not in dist:
                            dist[neighbor] = curr_dist + 1
                            parent[neighbor].append(curr)
                            q.append(neighbor)
                        elif dist[neighbor] == curr_dist + 1:
                            parent[neighbor].append(curr)
        

        @lru_cache(100)
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]
            
            paths = []
            for prev in parent[word]:
                for path in backtrack(prev):
                    paths.append(path + [word])
            
            return paths
        
        return backtrack(endWord)