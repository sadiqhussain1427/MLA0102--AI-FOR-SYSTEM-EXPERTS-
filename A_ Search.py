def a_star():
    graph = {}
    heuristic = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        graph[node] = {}
        h = int(input(f"Enter heuristic value of {node}: "))
        heuristic[node] = h

        m = int(input(f"Enter number of neighbors of {node}: "))
        for j in range(m):
            neighbor = input("Enter neighbor: ")
            cost = int(input("Enter cost: "))
            graph[node][neighbor] = cost
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    open_list = [(heuristic[start], 0, start, [start])]
    closed = set()
    while open_list:
        open_list.sort()
        f, g, current, path = open_list.pop(0)
        if current == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return
        closed.add(current)
        for neighbor in graph[current]:
            if neighbor not in closed:
                new_g = g + graph[current][neighbor]
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))
    print("Goal not reachable")
a_star()
