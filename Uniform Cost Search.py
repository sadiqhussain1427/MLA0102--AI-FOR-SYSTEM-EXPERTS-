import heapq
def uniform_cost_search():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        graph[node] = []
        m = int(input(f"Enter number of neighbors of {node}: "))
        for j in range(m):
            neighbor = input("Enter neighbor: ")
            cost = int(input("Enter cost: "))
            graph[node].append((neighbor, cost))
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            print("Path found:", path)
            print("Total cost:", cost)
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    print("Goal not reachable")

uniform_cost_search()
