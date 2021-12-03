import sys


def journeyToMoon(astronauts_number, pairs):
    sys.setrecursionlimit(1500)
    if astronauts_number == 1:
        return 1
    visited = [False] * astronauts_number
    sets = []
    graph = {i: [] for i in range(astronauts_number)}
    for (first_astro, second_astro) in pairs:
        graph[first_astro].append(second_astro)
        graph[second_astro].append(first_astro)

    for i in range(astronauts_number):
        if visited[i]:
            continue
        sets.append(dfs(i, graph, visited))

    answer = 0
    summ = 0
    for i in sets:
        answer = answer + summ*i
        summ = summ + i
    return answer


def dfs(index, graph, visited):
    if visited[index]:
        return 0
    count = 1
    visited[index] = True
    for i in graph[index]:
        count = count + dfs(i, graph, visited)
    return count


sys.setrecursionlimit(1500)
(astro, pairs_n) = map(int, input().strip().split())
pairs_arr = []
for _ in range(pairs_n):
    pairs_arr.append(list(map(int, input().strip().split())))
print(journeyToMoon(astro, pairs_arr))
