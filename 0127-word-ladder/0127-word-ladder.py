class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        g = defaultdict(list)
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                g[pattern].append(word)

        while q:
            curr, moves = q.popleft()
            if curr == endWord:
                return moves
            for i in range(len(curr)):
                pattern = curr[:i] + "*" + curr[i + 1:]
                for word in g[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word, moves + 1))

        return 0 