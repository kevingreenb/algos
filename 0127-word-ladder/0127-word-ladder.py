class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        g = defaultdict(list)
        visited = set([beginWord])
        q = deque([(beginWord, 1)])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)

        while q:
            cur, moves = q.popleft()
            if cur == endWord:
                return moves
            for i in range(len(cur)):
                pattern = cur[:i] + "*" + cur[i+1:]
                for word in g[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word, moves + 1))
        return 0        