from math import sqrt


def distance(p1, p2):
    x0 = p1[0] - p2[0]
    y0 = p1[1] - p2[1]
    return x0 * x0 + y0 * y0


def shouting(points):
    distances = []
    for i in range(len(points)):
        min_distance = 2 ** 31
        for j in range(i + 1, len(points)):
            min_distance = min(min_distance, distance(points[i], points[j]))
        distances.append(min_distance)
    return sqrt(max(distances))


points_count = int(input().strip())
points_arr = []
for _ in range(points_count):
    points_arr.append(list(map(int, input().strip().split())))
print(shouting(points_arr))
