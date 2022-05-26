import random


# random.seed(123)

class Puzzle:
    def __init__(self):
        self.true_board = [[1,2,3],[4,5,6],[7,8,9]]
        self.winner = [[1,2,3],[4,5,6],[7,8,0]]
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.empty = []
        self.moves = 0

    def generate_board(self):
        random_pos = random.sample([1,2,3,4,5,6,7,8,0], k=9)
        k = 0
        for i in range(3):
            for j in range(3):
                self.board[i][j] = random_pos[k]
                if self.board[i][j] == 0:
                    self.empty = [i,j]
                k += 1

    def print_board(self):
        for i in range(3):
            print(end='|')
            for j in range(3):
                if self.board[i][j] != 0:
                    print(self.board[i][j], end='|')
                else:
                    print(" ", end='|')
            print()

    def get_inv_count(self):
        inv_count = 0
        for row in self.board:
            for i in range(3-1):
                for j in range(i+1,3):
                    if row[j] != 0 and row[i] != 0 and row[i] > row[j]:
                        inv_count += 1
        return inv_count

    def is_solvable(self):
        inv_count = self.get_inv_count()
        if inv_count % 2 == 0:
            return True
        return False

    def search_channel(self, n):
        row, col = 0, 0
        for i in range(3):
            for j in range(3):
                if self.true_board[i][j] == n:
                    row, col = i, j
                    break
        return row, col

    def is_empty(self, n_channel):
        # find n_channel in true board
        flag = False
        i, j = self.search_channel(n_channel)
        if self.board[i][j] == 0:
            flag = True
        return flag

    # s -> source
    def shift(self, s):
        # get directions
        dirs = [(0,-1), (0,1), (-1,0), (1,0)]
        
        candidates = []
        cand_pos = []
        for d in dirs:
            row = self.empty[0] + d[0]
            col = self.empty[1] + d[1]
            if row >= 0 and row < 3:
                if col >= 0 and col < 3:
                    candidates.append(self.board[row][col])
                    cand_pos.append([row, col])
        
        updated = False
        for cand, pos in zip(candidates, cand_pos):
            if cand == s:
                self.board[self.empty[0]][self.empty[1]] = s
                self.board[pos[0]][pos[1]] = 0
                self.empty = [pos[0],pos[1]]
                self.moves += 1
                updated = True
                break

        return f"Moved {s}" if updated else f"Invalid move. Choose again" 

    def won(self):
        if self.board == self.winner:
            return True
        return False

if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.generate_board()
    while puzzle.is_solvable() == False:
        puzzle.generate_board()
    while True:
        puzzle.print_board()
        if puzzle.won():
            print(f"You solved it! Moves you took : {puzzle.moves}")
            break
        s = int(input("Enter channel : "))
        print(puzzle.shift(s))
        print()
