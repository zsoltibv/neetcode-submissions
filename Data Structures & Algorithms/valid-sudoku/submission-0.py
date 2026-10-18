class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        square_map = defaultdict(set)

        for i in range(9):
            line_set = set()
            col_set = set()
            
            for j in range(9):
                if board[i][j] in line_set:
                    return False

                if board[j][i] in col_set:
                    return False

                if board[i][j] != '.':
                    line_set.add(board[i][j])

                    # check sub squares
                    key: tuple = (i//3, j//3)
                    if board[i][j] in square_map[key]:
                         return False
                    
                    square_map[key].add(board[i][j])

                if board[j][i] != '.':
                    col_set.add(board[j][i])

        return True