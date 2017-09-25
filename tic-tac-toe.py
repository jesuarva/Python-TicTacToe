#Defining MAIN board
board ="""
*---------------*
|               |
    {a} | {b} | {c}
   ---+---+---
    {d} | {e} | {f}
   ---+---+---
    {g} | {h} | {i}
|               |
*---------------*
"""

#Defining the positjons on board.
#dict(positon) = how current game is going
#dict(available) = available positions in current game
position = {'a': ' ', 'b': ' ', 'c': ' ',
			'd': ' ', 'e': ' ', 'f': ' ',
			'g': ' ', 'h': ' ', 'i': ' '}
available = {'a': 'a', 'b': 'b', 'c': 'c',
			'd': 'd', 'e': 'e', 'f': 'f',
			'g': 'g', 'h': 'h', 'i': 'i'}
win_row_column = {'a': '1-1', 'b': '1-2', 'c': '1-3',
	   'd': '2-1', 'e': '2-2', 'f': '2-3',
	   'g': '3-1', 'h': '3-2', 'i': '3-3'}
win_check = {'p11': '', 'p12': '', 'p13': '',
			 'p21': '', 'p22': '', 'p23': '',
			 'p31': '', 'p32': '', 'p33': ''}
# row = [1]
# column = [3]
# # check = str(row[0])+str(column[0])
# win_check[str(row[0])+str(column[0])] = 'X'
# print win_check
# win_row.append(win['f'][0])
# win_column.append(win['f'][2])
	# type(win['a'])
# print str(win['33'])

# board_available = board.format(**available)
def board_game():
	print '''\n  ON GOING GAME'''+board.format(**position)
	return ''

def board_available():
	print '''\n  chose available'''+board.format(**available)
	return ''

# print board_game()
# print 'Select a position in the board for the next move:\nTo selct the position type the letter to chose it'+board_available

# To set current player.
# TODO def select_input():
player = ['O']
winner = [False]
row = [0,'','','']
column = [0,'','','']

# Set next move
# TODO check input is correct
def next_move():
	# next_move = 'f'
	next_move = raw_input(str(player[0])+"""'s turn.
Chose available position in the board
and hit enter:\n""")
	position[next_move] = player[0]
	# print position
	available[next_move] = ' '
	# print available
	row[0] = win_row_column[next_move][0]
	column[0] = win_row_column[next_move][2]
	win_check['p'+str(row[0])+str(column[0])] = player[0]
	# print board_available
	# print board.format(**available)	

def is_winner():
	for i in range(1,4):
		# print i
		row[i] = win_check['p'+str(row[0])+str(i)]
		column[i] = win_check['p'+str(i)+str(column[0])]
	# print row
	# print column
	row_check = set(row[1:4])
	column_check = set(column[1:4])
	# print len(row_check)
	# print row_check
	# print len(column_check)
	# print column_check
	if len(row_check) == 1 or len(column_check) ==1:
		winner[0] = True
		# print is_winner
		# print player[0]+' win!!'

def change_player():
	if player[0] == 'X':
		player[0] = 'O'
	else:
		player[0] = 'X'

def game():
	print '''Welcome to Tic-Tac-Toe by jesuarva.
First player's move goes with "X", the Second player goes with "O"'''
	while winner[0] != True:
		change_player()
		board_game()
		board_available()
		next_move()
		is_winner()
	print '''
GAME OVER:
And the winner is: '''+player[0]

game()