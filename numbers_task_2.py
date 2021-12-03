def f(a, i, zeroes, ones):
    if i == len(a):
        return 0
    z, o = a[i].count('0'), a[i].count('1')
    take = 0
    if zeroes >= z and ones >= o:
        take = 1 + f(a, i + 1, zeroes - z, ones - o)
    skip = f(a, i + 1, zeroes, ones)
    return max(take, skip)

data = "3 2 4\n00\n110\n101"
(n, zeroes, ones) = 3, 2, 4 # map(int, input().strip().split())
a = ["00", "110", "101"]
#for _ in range(n):
    #a.append(input().strip())
print(f(a, 0, zeroes, ones))
