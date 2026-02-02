def alphabeta(depth, node, is_max, values, alpha, beta):
 if depth == 0:
        return values[node]

    if is_max:
        best = -9999
        for i in range(2):
            val = alphabeta(depth-1, node*2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 9999
        for i in range(2):
            val = alphabeta(depth-1, node*2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

leaf_values = []
n = int(input("Enter number of leaf nodes (power of 2): "))

print("Enter leaf node values:")
for i in range(n):
    leaf_values.append(int(input()))

depth = int(input("Enter depth of tree: "))

result = alphabeta(depth, 0, True, leaf_values, -9999, 9999)
print("\nOptimal value using Alpha-Beta Pruning:", result)
