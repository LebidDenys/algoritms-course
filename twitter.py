from typing import List
import time


def sortTweets(tweetsArr: List[List[int]]) -> List[int]:
	res = []
	currentIndexes = [0]*len(tweetsArr)
	sumLen = 0
	for tweetsArrItem in tweetsArr:
		sumLen = sumLen + len(tweetsArrItem)
	for i in range(min(10, sumLen)):
		maxCurrentTweet, indexMaxCurrentTweet = {'createdAt': 0}, 0
		for j in range(len(tweetsArr)):
			if len(tweetsArr[j]) == 0:
				continue
			if tweetsArr[j][currentIndexes[j]]['createdAt'] > maxCurrentTweet['createdAt']:
				indexMaxCurrentTweet = j
				maxCurrentTweet = tweetsArr[j][currentIndexes[j]]
		currentIndexes[indexMaxCurrentTweet] += 1
		if currentIndexes[indexMaxCurrentTweet] == len(tweetsArr[indexMaxCurrentTweet]):
			tweetsArr[indexMaxCurrentTweet] = []
		res.append(maxCurrentTweet['id'])
	return res


class Twitter:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.users = {}

	def postTweet(self, userId: int, tweetId: int) -> None:
		"""
		Compose a new tweet.
		"""
		self.createUserIfRequired(userId)
		self.users[userId]['tweets'].insert(0, {'id': tweetId, 'createdAt': time.time()})

	def getNewsFeed(self, userId: int) -> List[int]:
		"""
		Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
		"""
		if userId not in self.users:
			return []
		unsortedTweets = [self.users[userId]['tweets']]
		for followee in self.users[userId]['following']:
			unsortedTweets.append(self.users[followee]['tweets'])
		return sortTweets(unsortedTweets)

	def follow(self, followerId: int, followeeId: int) -> None:
		"""
		Follower follows a followee. If the operation is invalid, it should be a no-op.
		"""
		self.createUserIfRequired(followerId)
		if followeeId not in self.users[followerId]['following']:
			self.createUserIfRequired(followeeId)
			self.users[followerId]['following'].append(followeeId)

	def unfollow(self, followerId: int, followeeId: int) -> None:
		"""
		Follower unfollows a followee. If the operation is invalid, it should be a no-op.
		"""
		if followerId in self.users and followeeId in self.users[followerId]['following']:
			self.users[followerId]['following'].remove(followeeId)

	def createUserIfRequired(self, userId: int) -> None:
		if userId not in self.users:
			self.users[userId] = {'tweets': [], 'following': []}


twitter = Twitter()
twitter.postTweet(2,5)
twitter.postTweet(1,3)
twitter.postTweet(1,101)
twitter.postTweet(2,13)
twitter.postTweet(2,10)
twitter.postTweet(1,2)
twitter.postTweet(2,94)
twitter.postTweet(2,505)
twitter.postTweet(1,333)
twitter.postTweet(1,22)
twitter.getNewsFeed(2)
twitter.follow(2,1)
print(twitter.getNewsFeed(2))
# ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet"
# ,"postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
# [[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2]
# ,[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]
# Output
# [null,null,null,null,null,null,null,null,null,null,null,[505,94,10,13,5],null,[505,94,22,333,10,13,5,2,101,3]]
# Expected
# [null,null,null,null,null,null,null,null,null,null,null,[505,94,10,13,5],null,[22,333,505,94,2,10,13,101,3,5]]