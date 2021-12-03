from math import *


def beautifulQuadruples(a, b, c, d):
	s = [a, b, c, d]
	s.sort()
	a, b, c, d = s
	max_v = 2 ** (ceil(log(d + 1, 2))) + 1  # max value of k^l
	dp = [[0 for i in range(max_v)] for j in range(c + 2)]
	dp2 = [0 for i in range(c + 2)]

	for k in range(c, 0, -1):
		for kl in range(max_v):
			dp[k][kl] = dp[k + 1][kl]
		for l in range(k, d + 1):
			dp[k][k ^ l] += 1
	for k2 in range(1, c + 1):
		for kl in range(max_v):
			dp2[k2] += dp[k2][kl]

	ans = 0
	for i in range(1, a + 1):
		for j in range(i, b + 1):
			# how many k,l st i^j^k^l!=0
			# find k^l!=i^j and l>=k>=j
			# dp2[j] => Number of pairs (k,l) st l>=k>=j
			# dp[j][i^j] => Number of pairs (k,l) st l>=k>=j and k^l == i^j
			# dp2[j] - dp[j][i^j] => Number of pairs (k,l) st l>=k>=j and k^l != i^j
			ans += dp2[j] - dp[j][i ^ j]
	return ans


print(beautifulQuadruples(1,2,3,4))

