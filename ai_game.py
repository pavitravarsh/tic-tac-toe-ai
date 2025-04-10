# ai_game.py

# Implementing Min-Max algorithm with Alpha-Beta Pruning
import random

def is_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: return True
    return False

def is_full(board):
    return all(cell != "" for row in board for cell in row)

def minmax(board, depth, alpha, beta, is_maximizing, player):
    if is_winner(board, 'X'): return -10 + depth
    if is_winner(board, 'O'): return 10 - depth
    if is_full(board): return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'O'
                    eval = minmax(board, depth + 1, alpha, beta, False, player)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'X'
                    eval = minmax(board, depth + 1, alpha, beta, True, player)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha: break
        return min_eval

def best_move(board, player):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = 'O'
                move_val = minmax(board, 0, -float('inf'), float('inf'), False, player)
                board[i][j] = ""
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move
