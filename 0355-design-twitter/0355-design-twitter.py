class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1 
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if self.tweets[followee]:
                time, tweetId = self.tweets[followee][-1]
                idx = len(self.tweets[followee]) - 1
                heapq.heappush(heap, (time, tweetId, followee, idx))

        res = []
        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                next_time, next_tweet = self.tweets[user][idx - 1]
                heapq.heappush(
                    heap,
                    (next_time, next_tweet, user, idx - 1)
                )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
