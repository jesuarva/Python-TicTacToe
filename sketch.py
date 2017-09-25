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

position = {'a': ' ', 'b': ' ', 'c': ' ',
			'd': ' ', 'e': ' ', 'f': ' ',
			'g': ' ', 'h': ' ', 'i': ' '}
available = {'a': 'a', 'b': 'b', 'c': 'c',
			'd': 'd', 'e': 'e', 'f': 'X',
			'g': 'g', 'h': 'h', 'i': 'i'}
win_row_column = {'a': '1-1', 'b': '1-2', 'c': '1-3',
	              'd': '2-1', 'e': '2-2', 'f': '2-3',
	              'g': '3-1', 'h': '3-2', 'i': '3-3'}
win_check = {'p11': 'X', 'p12': 'O', 'p13': '',
			 'p21': 'X', 'p22': 'X', 'p23': 'X',
			 'p31': '', 'p32': 'X', 'p33': ''}

# board_available = board.format(**available)
player = ['X']
winner = [False]
row = [2,'','','']
column = [2,'','','']

print row
row[1] = win_check['p'+str(1)+str(row[0])]
print row

def is_winner():
	for i in range(1,4):
		print i
		row[i] = win_check['p'+str(row[0])+str(i)]
		column[i] = win_check['p'+str(i)+str(column[0])]
	print row
	print column
	row_check = set(row[1:4])
	column_check = set(column[1:4])
	print len(row_check)
	print row_check
	print len(column_check)
	print column_check
	if len(row_check) == 1 or len(column_check) ==1:
		print winner
		winner[0] = True
		print player[0]+' win!!'
is_winner()
print winner

def next_move():
	# next_move = 'f'
	next_move = raw_input(str(player[0])+"""'s turn.
Chose available position in the board for next move
Plese type the letter to chose it and hit enter\n"""+board.format(**available))
	position[next_move] = player[0]
	# print position
	available[next_move] = player[0]
	# print available
	row[0] = win_row_column[next_move][0]
	column[0] = win_row_column[next_move][2]
	win_check[str(row[0])+str(column[0])] = player[0]
	# print board_available
	# print board.format(**available)
# next_move()

def change_player():
	if player[0] == 'X':
		player[0] = 'O'
	else:
		player[0] = 'X'

	print player[0]
# change_player()