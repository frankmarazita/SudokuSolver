from Puzzle import Puzzle, importPuzzle, numUnset

puzzle = importPuzzle('puzzles/puzzle1')

def simpleSolve(puzzle):

    while True:
        for i in range(9):
            for j in range(9):
                number = puzzle.get(i, j)
                if number['value'] == 0:
                    for value in range(9):
                        found = False
                        if not found:
                            row = puzzle.getRow(i)
                            for r in row:
                                if r['value'] == value + 1:
                                    found = True
                                    break
                        if not found:
                            col = puzzle.getCol(j)
                            for c in col:
                                if c['value'] == value + 1:
                                    found = True
                                    break
                        if not found:
                            nine = puzzle.getNine(j, i)
                            for n in nine:
                                if n['value'] == value + 1:
                                    found = True
                                    break
                        if not found:
                            number['possible'].append(value + 1)

        num_added = 0
        for i in range(9):
            for j in range(9):
                number = puzzle.get(i, j)
                if len(number['possible']) == 1:
                    number['value'] = number['possible'][0]
                    num_added += 1
                number['possible'] = []

        if num_added == 0:
            break

    return puzzle

print(simpleSolve(puzzle))
print('Solved:', puzzle.isWin())
