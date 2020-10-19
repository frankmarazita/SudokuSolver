import csv

class Puzzle:

    def __init__(self):
        self.values = []

    def get(self, x, y):
        return self.values[x][y]

def importPuzzle(file):
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        puzzle = Puzzle()
        for row in data:
            dict_row = []
            for i in row:
                dict_row.append({'value': i, 'static': i != "0"})
            puzzle.values.append(dict_row)
        return puzzle

def isWin(puzzle):
    for i in range(9):
        row = []
        for j in range(9):
            row.append(puzzle.get(i, j)['value'])
        for j in range(9):
            if str(j + 1) not in row:
                return False

    for i in range(9):
        col = []
        for j in range(9):
            col.append(puzzle.get(j, i)['value'])
        for j in range(9):
            if str(j + 1) not in col:
                return False

    for i in range(3):
        for j in range(3):
            nine = []
            for k in range(3):
                for l in range(3):
                    nine.append(puzzle.get(k + i * 3, l + j * 3)['value'])
            for k in range(9):
                if str(k + 1) not in nine:
                    return False

    return True

puzzle = importPuzzle('puzzle1')

num_unset = 0

for i in range(9):
    for j in range(9):
        item_dict = puzzle.get(i, j)
        if not item_dict['static']:
            num_unset += 1

print(num_unset)

print(isWin(puzzle))
