# Description: This file contains the game logic for the Tic Tac Toe game.
from .AI import AI
class TicTacToe:
    def __init__(self, ai_instance):
        self.board = [   0, 1, 2, 
                         3, 4, 5, 
                         6, 7, 8
                                    ]
        self.turn = 0
        self.human = "O"
        self.AI = "X"
        self.ai_instance = ai_instance
        self.winner = None
        

        
    
    def turns(self):
        self.turn += 1



    def check_winner(self, board):

        possible_wins = [ [0, 1, 2], 
                          [3, 4, 5], 
                          [6, 7, 8], 
                          [0, 3, 6], 
                          [1, 4, 7], 
                          [2, 5, 8], 
                          [0, 4, 8], 
                          [2, 4, 6] ]
        winner = None
        available_moves = 0
        for win in possible_wins:
            if board[win[0]] == board[win[1]] == board[win[2]]:
                winner = board[win[0]]
                return winner 
        else:
            for i in board:
                if type(i) == int:
                    available_moves += 1    

        if winner == None and available_moves == 0:
            return "Draw"
            
        return winner 


    def play(self, human_move):
        p1 = self.ai_instance
    
        if self.turn % 2 == 0:
            p1_move = p1.best_AI_move(self.board)
            self.board[p1_move] = "X"
            result = self.check_winner(self.board)  
            self.winner = result
            self.turns()
             

        else:
            p2 = int(human_move)
            self.board[p2] = "O"
            result = self.check_winner(self.board)
            self.winner = result
            self.turns()

        return result

    def get_board(self): #returns the board in a dictionary format
        board_dict = {}
        for i in range(len(self.board)):
            board_dict[f"cell_{i}"] = self.board[i]

        return board_dict