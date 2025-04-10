# app.py

from flask import Flask, render_template, jsonify, request
from ai_game import best_move, is_winner, is_full

app = Flask(__name__)

# Initial empty Tic-Tac-Toe board
board = [['' for _ in range(3)] for _ in range(3)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_move', methods=['POST'])
def get_move():
    global board
    player_move = request.json['move']  # Player move (row, col)
    row, col = player_move

    # Update the board with the player's move
    if board[row][col] == '':
        board[row][col] = 'X'

        # Check if player wins
        if is_winner(board, 'X'):
            return jsonify({'board': board, 'game_over': True, 'message': 'Player Wins!'})

        # If the board is full, game over
        if is_full(board):
            return jsonify({'board': board, 'game_over': True, 'message': 'It\'s a draw!'})

        # AI Move
        ai_move = best_move(board, 'O')
        board[ai_move[0]][ai_move[1]] = 'O'

        # Check if AI wins
        if is_winner(board, 'O'):
            return jsonify({'board': board, 'game_over': True, 'message': 'AI Wins!'})

        return jsonify({'board': board, 'game_over': False, 'message': ''})
    return jsonify({'board': board, 'game_over': False, 'message': 'Invalid Move!'})

@app.route('/reset', methods=['POST'])
def reset():
    global board
    board = [['' for _ in range(3)] for _ in range(3)]
    return jsonify({'board': board, 'game_over': False, 'message': 'Game reset!'})

if __name__ == "__main__":
    app.run(debug=True)
