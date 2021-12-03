def roadsAndLibraries(cities, lib_cost, road_cost, roads):
    if road_cost > lib_cost:
        return cities * lib_cost
    else:
        graph = {i: [] for i in range(1, cities + 1)}
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])

        visited = [False] * (cities + 1)
        count_components = 0
        list_components = []
        for i in range(1, cities + 1):
            if not visited[i]:
                value = 0
                count_nodes = dfs(i, graph, visited, value)
                count_components += 1
                list_components.append(count_nodes)
        total = 0
        for i in list_components:
            total += (road_cost * (i - 1))
        return total + count_components * lib_cost


def dfs(index, graph, visited, value):
    visited[index] = True
    value += 1
    for i in graph[index]:
        if not visited[i]:
            value = dfs(i, graph, visited, value)
    return value


number_of_queries = int(input().strip())
for _ in range(number_of_queries):
    (n_cities, n_roads, lib_cost_arg, road_cost_arg) = map(int, input().strip().split())
    roads_arg = []
    for __ in range(n_roads):
        roads_arg.append(list(map(int, input().strip().split())))
    print(roadsAndLibraries(n_cities, lib_cost_arg, road_cost_arg, roads_arg))
