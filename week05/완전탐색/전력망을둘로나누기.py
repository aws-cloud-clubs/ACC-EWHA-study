from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    min_diff = n

    for i in range(len(wires)):
        # [[i번째 노드랑 연결된 노드들], [], [], [], [], [], [], []]
        graph = [[] for _ in range(n + 1)] 

        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        count = bfs(1, graph, visited)

        diff = abs(n - count - count)  # count: 한쪽 / n-count = 다른 한쪽
        min_diff = min(min_diff, diff)

    return min_diff
