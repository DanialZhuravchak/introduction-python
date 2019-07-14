game = [[2, 1, 1, ],
        [2, 2, 0, ],
        [2, 2, 0, ]]


def win(current_game):
    '''Horizontal
    '''
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] ! = 0:
            print(f"Player {row[0]} is the winner horizontally!")

    '''Diaginal
    '''
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonaly (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonaly (\\)!")

    '''Vertical
    '''

    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner virtically (|)!")

win(game)
