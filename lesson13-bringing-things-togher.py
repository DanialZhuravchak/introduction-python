import itertools

game = [[2, 1, 1, ],
        [1, 2, 0, ],
        [2, 1, 2, ]]


def win(current_game):
    '''Horizontal
    '''
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
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


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("  0  1  2")
        if not just_display:
                game[row][column] = player
        for count, row in enumerate(game):
                print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/colomn as 0 1 or 2", e)

    except Exception as e:
        print("Something went very wrong!", e)


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0, ],
            [0, 0, 0, ],
            [0, 0, 0, ]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choise = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choise)
        print(f"Current Player: {current_player}")
        column_choise = int(input("What column do you want to play? (0, 1, 2): "))
        row_choise = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choise, column_choise)
