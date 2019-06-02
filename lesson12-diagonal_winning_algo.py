game = [[2, 1, 1, ],
        [2, 2, 0, ],
        [2, 2, 0, ],]


diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

'''
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

print(diags)

'''


'''
for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])



if check.count(check[0]) == len(check) and check[0] != 0:
    print("Winner!")
'''

'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")

win(game)
'''