import numpy as np
import lib
# note first and second are combined
def code():
    def path_finder(row, col, direction, row_wise, col_wise, width, height):
        path = set()
        simple_path = set()
        while True:
            if (row, col, direction) in path:
                return False, path
            path.add((row, col, direction))
            simple_path.add((row, col))
            if direction == 'up':
                if row == 0:
                    break
                if row - 1 in col_wise[col]:
                    # turn clockwise
                    direction = 'right'
                else:
                    row -= 1
            elif direction == 'right':
                if col == width - 1:
                    break
                if col + 1 in row_wise[row]:
                    direction = 'down'
                else:
                    col += 1
            elif direction == 'down':
                if row == height - 1:
                    break
                if row + 1 in col_wise[col]:
                    direction = 'left'
                else:
                    row += 1
            else:
                if col == 0:
                    break
                if col - 1 in row_wise[row]:
                    direction = 'up'
                else:
                    col -= 1
        return True, simple_path
    
    map_rows = lib.records(6, '')
    row_wise = {}
    col_wise = {}
    for row, map_row in enumerate(map_rows):
        print(map_row)
        row_wise[row] = []
        for col, c in enumerate(map_row.strip()):
            if col not in col_wise:
                col_wise[col] = []
            if c == '#':
                print(row, col)
                row_wise[row].append(col)
                col_wise[col].append(row)                
            if c == '^':
                start_row, start_col = row, col
    width = len(col_wise)
    height = len(row_wise)
    print(width, height)
    print(col_wise)
    print(row_wise)
    print(start_row, start_col)
    
    print("First")
    is_out, path = path_finder(start_row, start_col, 'up', row_wise, col_wise, width, height)
    #print(path)
    result = len(path)
    print(is_out, result)
    print("Second")
    path.remove((start_row, start_col))
    result = 0
    for step_row, step_col in path:
        row_wise[step_row].append(step_col)
        col_wise[step_col].append(step_row)
        is_out, _ = path_finder(start_row, start_col, 'up', row_wise, col_wise, width, height)
        row_wise[step_row].remove(step_col)
        col_wise[step_col].remove(step_row)
        result += 0 if is_out else 1
    print (result)
import timeit
print(timeit.timeit(code, number=1))