#Indexes and Slices
game = [[0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],]

def game_board(player, row, column, just_display=False):
        print("  0  1  2")
        if not just_display:
                game[row][column] = player
        for count, row in enumerate(game):
                print(count, row)

game_board(1,10,0)
#game[0][1] = 1
#game_board()