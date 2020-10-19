import csv

class Puzzle:

    def __init__(self):
        self.values = []

    def get(self, x, y):
        return self.values[x][y]

    def getCol(self, index):
        col = []
        for i in range(9):
            col.append(self.get(i, index))
        return col

    def getRow(self, index):
        row = []
        for i in range(9):
            row.append(self.get(index, i))
        return row

    def getNine(self, x, y):

        i = 0
        j = 0

        if y < 3:
            i = 0
        elif y < 6:
            i = 1
        elif y < 9:
            i = 2

        if x < 3:
            j = 0
        elif x < 6:
            j = 1
        elif x < 9:
            j = 2

        nine = []
        for k in range(3):
            for l in range(3):
                nine.append(self.get(k + i * 3, l + j * 3))
        return nine

    def __str__(self):
        string = ""
        for i in range(9):
            for j in range(9):
                value = self.get(i, j)['value']
                if value == 0:
                    value = " "
                string += str(value) + " "
            string += "\n"
        return string

    def isWin(self):
        for i in range(9):
            row = []
            for j in range(9):
                row.append(self.get(i, j)['value'])
            for j in range(9):
                if j + 1 not in row:
                    return False

        for i in range(9):
            col = []
            for j in range(9):
                col.append(self.get(j, i)['value'])
            for j in range(9):
                if j + 1 not in col:
                    return False

        for i in range(3):
            for j in range(3):
                nine = []
                for k in range(3):
                    for l in range(3):
                        nine.append(self.get(k + i * 3, l + j * 3)['value'])
                for k in range(9):
                    if k + 1 not in nine:
                        return False
        return True

def importPuzzle(file):
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        puzzle = Puzzle()
        for row in data:
            dict_row = []
            for i in row:
                dict_row.append({'value': int(i), 'static': i != "0", 'possible': []})
            puzzle.values.append(dict_row)
        return puzzle

def numUnset(puzzle):
    num_unset = 0
    for i in range(9):
        for j in range(9):
            item_dict = puzzle.get(i, j)
            if not item_dict['static']:
                num_unset += 1
    return num_unset
