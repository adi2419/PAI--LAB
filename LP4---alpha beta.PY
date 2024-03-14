MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminal condition: If depth reaches 3, return the value of the node
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        # Maximize for the maximizing player
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        # Minimize for the minimizing player
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

# Driver Code
if __name__ == "__main__":
    values = [10, 9, 14, 18, 5, 4, 50, 3]
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
