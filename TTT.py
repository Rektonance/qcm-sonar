class TTTGame:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
    
    def set_mark(self, mark:int, pos:tuple[int]):
        if self.board[pos[0], pos[1]] != 0 or mark not in [1,2]:
            return -1
        self.board[pos[0], pos[1]] = mark
        return 0