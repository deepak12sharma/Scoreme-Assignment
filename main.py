# ### 2. main.py

# ```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for i in range(n):
        for j, _ in graph[i]:
            in_degree[j] += 1

    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        for adjacent, _ in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return topo_order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    distance = [-float('inf')] * n
    distance[topo_order[0]] = 0

    for node in topo_order:
        for adjacent, weight in graph[node]:
            if distance[node] + weight > distance[adjacent]:
                distance[adjacent] = distance[node] + weight

    return max(distance)

#I think there is a problem with the output of graph 4. There are no self-loops, yet the longest path is 3. It should be 2.