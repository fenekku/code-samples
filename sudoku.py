

def square_elements(row, col, puzzle):
    t = (row / 3) * 3
    l = (col / 3) * 3
    return set([e for r in puzzle[t:t+3] for e in r[l:l+3]])

def col_elements(col, puzzle):
    return set([row[col] for row in puzzle])

def row_elements(row, puzzle):
    return set(puzzle[row])

def choices(row, col, puzzle):
    possibilities = set(range(1,10))
    possibilities -= row_elements(row, puzzle)
    possibilities -= col_elements(col, puzzle)
    possibilities -= square_elements(row, col, puzzle)
    return list(possibilities)

def valid(puzzle):
    for i in xrange(9):
        if sum(row_elements(i, puzzle)) != 45: return False
        if sum(col_elements(i, puzzle)) != 45: return False
    for r, c in zip([0,0,0,3,3,3,6,6,6],[0,3,6,0,3,6,0,3,6]):
        if sum(square_elements(r, c, puzzle)) != 45: return False
    return True

def sudoku(puzzle):
    while not valid(puzzle):
        for r, row in enumerate(puzzle):
            for c, v in enumerate(row):
                if v != 0: continue
                options = choices(r,c, puzzle)
                if len(options) == 1:
                    puzzle[r][c] = options[0]
    return puzzle

def test_sudoku():
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    solution = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

    assert sudoku(puzzle) == solution
