
def code():
    import numpy as np
    print("First")
    window = np.genfromtxt([
            "S  S  S", 
            " A A A ",
            "  MMM  ",
            "SAMXMAS",
            "  MMM  ",
            " A A A ",
            "S  S  S", 
            ],dtype='S1', delimiter=1) 
    print(window)
    mask = np.array([
            [1,0,0,2,0,0,3],
            [0,1,0,2,0,3,0],
            [0,0,1,2,3,0,0],
            [4,4,4,0,5,5,5],
            [0,0,6,7,8,0,0],
            [0,6,0,7,0,8,0],
            [6,0,0,7,0,0,8],
            ])
    mask[mask != 0] = 4 ** (mask[mask != 0] - 1)
    print(mask)
    field = np.genfromtxt('inputs/4.txt', dtype='S1', delimiter=1)
    field = np.pad(field, pad_width=3, mode='constant', constant_values=b'.')
    result = 0
    for row in range(3, field.shape[0]-3):
        for col in range(3, field.shape[1]-3):
           if field[row, col] == b'X':
               masked = mask[window == field[row-3:row+4, col-3:col+4]]
               summed = masked.sum()
               while summed > 0:
                   result += 1 if summed % 4 == 3 else 0
                   summed = summed // 4
    print(result)
    print("Second")    
    window = np.genfromtxt([
            "M M",
            " A ",
            "S S",
            ],dtype='S1', delimiter=1) 
    # print(window)
    field = np.genfromtxt('inputs/4.txt', dtype='S1', delimiter=1)
    result = 0
    for row in range(1, field.shape[0]-1):
        for col in range(1, field.shape[1]-1):
            if field[row, col] == b'A':
                matched = ((window == field[row-1:row+2, col-1:col+2]).sum() == 5
                    or (np.rot90(window) == field[row-1:row+2, col-1:col+2]).sum() == 5
                    or (np.rot90(window, k=2) == field[row-1:row+2, col-1:col+2]).sum() == 5
                    or (np.rot90(window, k=3) == field[row-1:row+2, col-1:col+2]).sum() == 5
                )
                result += 1 if matched else 0    
    
    print (result)


import timeit
print(timeit.timeit(code, number=1))