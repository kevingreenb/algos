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

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)
        
        q = deque([(beginWord,1)])
        visited = set([beginWord])

        while q:
            current, moves = q.popleft()
            if current == endWord:
                return moves
            for i in range(len(current)):
                pattern = current[:i] + "*" + current[i+1:]
                for word in g[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word, moves+1))
        
        return 0
        