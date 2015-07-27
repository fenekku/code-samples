
def num_neighbours(r,c,cells):
    neighbours = [(r-1,tc) for tc in xrange(c-1,c+2)]
    neighbours += [(r+1,tc) for tc in xrange(c-1,c+2)]
    neighbours += [(r,c-1), (r,c+1)]
    out_row = len(cells)
    out_col = len(cells[0])
    n = 0
    for tr,tc in neighbours:
        if tr < 0 or tc < 0:
            continue
        if tr == out_row or tc == out_col:
            continue
        n += 1 if cells[tr][tc] == 1 else 0
    return n

def next_cell(r,c,cells):
    n = num_neighbours(r, c, cells)
    if cells[r][c] == 0 and n == 3:
        return 1
    elif n < 2 or n > 3:
        return 0
    else:
        return cells[r][c]

def next_gen(cells):
    next_cells = [[0 for _ in row] for row in cells]
    for r, row in enumerate(cells):
        for c, cell in enumerate(row):
            next_cells[r][c] = next_cell(r,c,cells)
    return next_cells

def test_next_gen():
    state = [[0,0,1],[0,1,0],[1,1,1],[1,0,0]]

    next_state = [[0,0,0],[1,0,0],[1,0,1],[1,0,0]]

    assert next_gen(state) == next_state
