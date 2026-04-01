class game_state():
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.white_to_move =True
        self.move_log =[]
    def make_move(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move
    '''undo move'''
    def undo_move(self):
        if len(self.move_log)!=0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col]=move.piece_moved
            self.board[move.end_row][move.end_col]= move.piece_captured
            self.white_to_move = not self.white_to_move
    def get_valid_moves(self):
        pass
    def get_all_posible_moves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == "P":
                        self.get_pawn(r,c,moves)
                    elif piece == "R":
                        self.get_rook(r,c,moves)
    '''get all pawn moves'''
                                   
class Move():
    ranks_to_rows = {"1":7, "2":6, "3":5, "4":4,"5":3, "6":2,"7":1,"8":0}
    Rows_to_ranks ={v:k for k,v in ranks_to_rows.items()}
    files_to_cols = {"a":0, "b":1, "c":2, "d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files ={v:k for k,v in files_to_cols.items()}
    def __init__(self,start_sq,end_sq,board):
        self.start_row , self.start_col = start_sq
        self.end_row, self.end_col = end_sq
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
    def get_chess_notation(self):
        return self.get_rank_files(self.start_row,self.start_col)+self.get_rank_files(self.end_row,self.end_col)
    


    def get_rank_files(self,r,c):
        return self.cols_to_files[c]+ self.rows_to_ranks[r]