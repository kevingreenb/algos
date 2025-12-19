class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.users = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.users[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        self.follows[userId].add(userId)
        h = []

        for followee in self.follows[userId]:
            if self.users[followee]:
                i = len(self.users[followee]) - 1
                heapq.heappush(h, (self.users[followee][i][0], self.users[followee], i))

        while h and len(ans) < 10:
            time, cur, i = heapq.heappop(h)
            ans.append(cur[i][1])

            if i > 0:
                i -= 1
                heapq.heappush(h, (cur[i][0], cur, i))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)