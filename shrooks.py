mod = 1000000007


def count(shrook, width):
	result = dp(shrook, width) + 1
	return result % mod


def dp(shrook, width):
	if width <= 0:
		return 0

	result = 0
	for i in range(width):
		result = result + 1 + dp(shrook, width - shrook - 1 - i)
	return (result - 1) % mod


print(count(3, 100))
