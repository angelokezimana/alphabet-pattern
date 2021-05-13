alphabets = {
    'A': [(-2, 1, -2), (1, -3, 1), (5, 0, 0), (1, -3, 1), (1, -3, 1)],
    'B': [(4, 0, 0), (1, -3, 1), (4, 0, 0), (1, -3, 1), (4, 0, 0)],
    'C': [(-1, 0, 4), (1, 0, 0), (1, 0, 0), (1, 0, 0), (-1, 0, 4)],
    'D': [(4, 0, 0), (1, -3, 1), (1, -3, 1), (1, -3, 1), (4, 0, 0)],
    'E': [(5, 0, 0), (1, 0, 0), (5, 0, 0), (1, 0, 0), (5, 0, 0)],
    'F': [(5, 0, 0), (1, 0, 0), (5, 0, 0), (1, 0, 0), (1, 0, 0)],
    'G': [(5, 0, 0), (1, 0, 0), (1, -2, 2), (1, -3, 1), (5, 0, 0)],
    'H': [(1, -3, 1), (1, -3, 1), (5, 0, 0), (1, -3, 1), (1, -3, 1)],
    'I': [(1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)],
    'J': [(5, 0, 0), (-4, 0, 1), (-4, 0, 1), (-3, 0, 1), (2, 0, 0)],
    'K': [(1, -3, 1), (1, -2, 1), (2, 0, 0), (1, -2, 1), (1, -3, 1)],
    'L': [(1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (5, 0, 0)],
    'M': [(1, -3, 1), (2, -1, 2), (1, -1, 1, -1, 1), (1, -3, 1), (1, -3, 1)],
    'N': [(1, -3, 1), (2, -2, 1), (1, -1, 1, -1, 1), (1, -2, 2), (1, -3, 1)],
    'O': [(-1, 3, -1), (1, -3, 1), (1, -3, 1), (1, -3, 1), (-1, 3, -1)],
    'P': [(4, 0, 0), (1, -3, 1), (4, 0, 0), (1, 0, 0), (1, 0, 0)],
    'O': [(-1, 3, -1), (1, -3, 1), (1, -3, 1), (1, -3, 1), (-1, 3, -1)],
    'X': [(1, -3, 1), (1, -3, 1), (-2, 1, -2), (1, -3, 1), (1, -3, 1)],
}

for alphabet, items in alphabets.items():

    for x in items:

        z = ''
        for y in x:
            if y < 0:
                z += ' ' * abs(y)
            else:
                z += '*' * y

        print(z)

    print('----------------------')