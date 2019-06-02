game = [[2, 1, 1, ],
        [2, 2, 0, ],
        [2, 2, 0, ],]

check = []

for row in game:
    check.append(row[0])


if check.count(check[0]) == len(check) and check[0] != 0:
    print("Winner!")


'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")

win(game)
'''