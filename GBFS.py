def gbfs():
    graph = {}
    heuristic = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        heuristic[node] = int(input(f"Enter heuristic value of {node}: "))
        graph[node] = []
        m = int(input(f"Enter number of neighbors of {node}: "))
        for j in range(m):
            neighbor = input("Enter neighbor: ")
            graph[node].append(neighbor)
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    open_list = [(heuristic[start], start, [start])]
    visited = set()
    while open_list:
        open_list.sort()   
        h, current, path = open_list.pop(0)
        if current == goal:
            print("Path found:", path)
            return
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                open_list.append(
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )
    print("Goal not reachable")
gbfs()
