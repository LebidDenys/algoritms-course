# def evenForest(nodes, t_edges, edges):
#     weight = {i: 0 for i in range(1, nodes + 1)}
#     for i in range(t_edges-1,-1,-1):
#         weight[edges[i][0]] += 1
#         weight[edges[i][1]] += 1
#     result = 0
#     # for weight_key in weights:
#     #     if weights[weight_key] % 2 == 0:
#     #         result += 1
#     # return result
#     return(len([1 for key in weight if weight[key]%2==0]))

def createGraph(t_from,t_to):
    d = defaultdict(set)
    for u,v in zip(t_from,t_to):
        d[v].add(u)
    return d

def countNodes(d,node,count):
    if node not in d or len(d[node]) == 0:
        return count
    for nei in d[node]:
        count = countNodes(d,nei,count+1)
    return count



def evenForest(t_nodes, t_edges, t_from, t_to):
    d = createGraph(t_from,t_to)
    countDict = {}
    for i in range(1,t_nodes+1):
        count = countNodes(d,i,1)
        countDict[i] = count
    ans = -1
    for i in countDict.values():
        if i >= 2 and i % 2 == 0:
            ans += 1
    return ans


(nodes_number_arg, edges_number_arg) = map(int, input().strip().split())
edges_arr = []
for i in range(edges_number_arg):
    edges_arr.append(list(map(int, input().strip().split())))
print(evenForest(nodes_number_arg, edges_number_arg, edges_arr))
