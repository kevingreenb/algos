class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        g = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            cur, moves = q.popleft()

            if cur == endWord:
                return moves

            for i in range(len(cur)):
                pattern = cur[:i] + "*" + cur[i+1:]
                for word in g[pattern]:
                    if word not in visited:
                        q.append((word, moves + 1))
                        visited.add(word)
        
        return 0
        