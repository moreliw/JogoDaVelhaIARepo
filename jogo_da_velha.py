import random

def copiaDoTabuleiro(board):
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def tabuleiro(board):
	tabuleiroCopia = copiaDoTabuleiro(board)
	for i in range(1,10):
		if(board[i] == ''):
			tabuleiroCopia[i] = str(i)
		else:
			tabuleiroCopia[i] = board[i]
	
	print(' ' + tabuleiroCopia[7] + ' | ' + tabuleiroCopia[8] + ' | ' + tabuleiroCopia[9])
	print(' ---------')
	print(' '+ tabuleiroCopia[4] + ' | ' + tabuleiroCopia[5] + ' | ' + tabuleiroCopia[6])
	print(' ---------')
	print(' '+ tabuleiroCopia[1] + ' | ' + tabuleiroCopia[2] + ' | ' + tabuleiroCopia[3])

def quemComeca():
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'jogador'

def movimento(tabuleiro, jogadorJogada, movimento):
	tabuleiro[movimento] = jogadorJogada

def temGanhador(tab, let):
	return((tab[7] == let and tab[8] == let and tab[9] == let) or
		(tab[4] == let and tab[5] == let and tab[6] == let) or 
		(tab[1] == let and tab[2] == let and tab[3] == let) or 
		(tab[7] == let and tab[4] == let and tab[1] == let) or 
		(tab[8] == let and tab[5] == let and tab[2] == let) or 
		(tab[9] == let and tab[6] == let and tab[3] == let) or 
		(tab[7] == let and tab[5] == let and tab[3] == let) or 
		(tab[9] == let and tab[5] == let and tab[1] == let)) 

def temEspacoVazio(tabuleiro, movimento):
	if(tabuleiro[movimento] == ''):
		return True
	else:
		return False

def movimentoJogador(tabuleiro):
	movimento = ''
	while movimento not in '1 2 3 4 5 6 7 8 9'.split() or not temEspacoVazio(tabuleiro, int(movimento)):
		print('')
		print('Vez do jogador (Escolha seu movimento)')
		movimento = input();
		if(movimento not in '1 2 3 4 5 6 7 8 9'):
			print("MOVIMENTO INVALIDO!")
		
		if(movimento in '1 2 3 4 5 6 7 8 9'):
			if(not temEspacoVazio(tabuleiro, int(movimento))):
				print("ESPAÇO INSDISPONÍVEL!") 

	return int(movimento)


def tabuleiroCheio(tabuleiro):
	for i in range(1, 10):
		if temEspacoVazio(tabuleiro, i):
			return False
	return True

def possiveisOpcoes(tabuleiro):
	opcoes = []

	for i in range(1, 10):
		if temEspacoVazio(tabuleiro, i):
			opcoes.append(i)

	return opcoes

def fimDeJogo(tabuleiro, computerLetter):
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if(temGanhador(tabuleiro, computerLetter)):
		return 1

	elif(temGanhador(tabuleiro, playerLetter)):
		return -1

	elif(tabuleiroCheio(tabuleiro)):
		return 0

	else:
		return None


def alphabeta(board, computerLetter, turn, alpha, beta):

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = fimDeJogo(board, computerLetter)

	if (finish != None):
		return finish

	possiveis = possiveisOpcoes(board)

	if turn == computerLetter:
		for move in possiveis:
			movimento(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			movimento(board, '', move)
			if val > alpha:
				alpha = val

			if alpha >= beta:
				return alpha
		return alpha

	else:
		for move in possiveis:
			movimento(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			movimento(board, '', move)
			if val < beta:
				beta = val

			if alpha >= beta:
				return beta
		return beta



def getComputerMove(board, turn, computerLetter):
	a = -2
	opcoes = []

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	for i in range(1, 10):
		copy = copiaDoTabuleiro(board)
		if temEspacoVazio(copy, i):
			movimento(copy, computerLetter, i)
			if temGanhador(copy, computerLetter):
				return i

	for i in range(1, 10):
		copy = copiaDoTabuleiro(board)
		if temEspacoVazio(copy, i):
			movimento(copy, playerLetter, i)
			if temGanhador(copy, playerLetter):
				return i

	possiveisOpcoesOn = possiveisOpcoes(board)

	for move in possiveisOpcoesOn:

		movimento(board, computerLetter, move)
		val = alphabeta(board, computerLetter, playerLetter, -2, 2)	

		movimento(board, '', move)
		if val > a:
			a = val
			opcoes = [move]

		elif val == a:
			opcoes.append(move)

	return random.choice(opcoes)

jogar = True

while jogar:
	theBoard = [''] * 10
	playerLetter, computerLetter = ['X','O']
	turn = quemComeca()
	print('')
	print(turn + ' começa:')
	print('')
	gameisPlaying = True

	while gameisPlaying:
		if turn == 'jogador':
			tabuleiro(theBoard)
			move = movimentoJogador(theBoard)
			movimento(theBoard, playerLetter, move)

			if temGanhador(theBoard, playerLetter):
				tabuleiro(theBoard)
				print('Woooow! Voce venceu o jogo!')
				gameisPlaying = False
			
			else:
				if tabuleiroCheio(theBoard):
					tabuleiro(theBoard)
					print('VELHA!')
					break
				else:
					turn = 'computador'

		else:
			move = getComputerMove(theBoard, playerLetter, computerLetter)
			movimento(theBoard, computerLetter, move)

			if temGanhador(theBoard, computerLetter):
				tabuleiro(theBoard)
				print("O computador venceu :(")
				gameisPlaying = False

			else:
				if tabuleiroCheio(theBoard):
					tabuleiro(theBoard)
					print()
					print('O jogo terminou empatado')
					print()
					break
				else:
					turn = 'jogador'

	letterNew = ''
	while not(letterNew == 'S' or letterNew == 'N'):
		print("Jogar Novamente? S ou N")
		letterNew = input().upper()
		if (letterNew != 'S' and letterNew != 'N'):
			print("Entrada invalida! Digite S (para sim) ou N (para não)!")
		if(letterNew == 'N'):
			print("FIM DE JOGO!")
			jogar = False





