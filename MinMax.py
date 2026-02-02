def minimax(depth, node, is_max, values):
    if depth == 0:
        return values[node]
    if is_max:
        best = -9999
        for i in range(2):
            val = minimax(depth-1, node*2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = 9999
        for i in range(2):
            val = minimax(depth-1, node*2 + i, True, values)
            best = min(best, val)
        return best
leaf_values = []
n = int(input("Enter number of leaf nodes (power of 2): "))
print("Enter leaf node values:")
for i in range(n):
    leaf_values.append(int(input()))
depth = int(input("Enter depth of tree: "))
result = minimax(depth, 0, True, leaf_values)
print("\nOptimal value using Minimax:", result)
