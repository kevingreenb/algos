from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        adj = defaultdict(list)
        dist = {beginWord: 0}
        wordSet.discard(beginWord)
        
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            current_level_visited = set()
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                for i in range(len(curr)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        next_word = curr[:i] + char + curr[i+1:]
                        
                        if next_word in wordSet:
                            if next_word not in dist:
                                dist[next_word] = dist[curr] + 1
                                current_level_visited.add(next_word)
                                queue.append(next_word)

                            if dist[next_word] == dist[curr] + 1:
                                adj[next_word].append(curr)
                                
                            if next_word == endWord:
                                found = True
            
            for w in current_level_visited:
                wordSet.discard(w)
        
        if not found:
            return []
            
        res = []
        def dfs(curr, path):
            if curr == beginWord:
                res.append(path[::-1])
                return
            
            for neighbor in adj[curr]:
                dfs(neighbor, path + [neighbor])

        dfs(endWord, [endWord])
        return res