# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network
# and is decoded back to the original list of strings.

# My solution
def encode(strs):
    string = ""

    for s in strs:
        string += str(len(s))
        string += "#"
        string += s

    return string


def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        word = s[j + 1: j + 1 + length]
        res.append(word)
        i = j + 1 + length
    return res

# You are given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its
# upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements
# of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# My solution
class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.matrix[i][j]
        return sum

# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid.

# My solution
def isValidSudoku(board):
    row_list = [set() for _ in range(9)]
    col_list = [set() for _ in range(9)]
    square_list = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if '0' <= board[i][j] <= '9':
                if board[i][j] in row_list[i]:
                    return False
                if board[i][j] in col_list[j]:
                    return False
                if board[i][j] in square_list[i//3 * 3 + j//3]:
                    return False
                row_list[i].add(board[i][j])
                col_list[j].add(board[i][j])
                square_list[i//3 * 3 + j//3].add(board[i][j])
    return True

print(isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))