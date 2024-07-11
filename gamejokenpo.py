from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-=-=- Vamos jogar JOKENPO -=-=-')
jogador = int(input('''Qual é a sua jogada?
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura '''))
print('-=' * 15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 20)
print('O computador jogou {}'.format(itens[computador]))
print('E o jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == jogador: # EMPATE
	print('JOGO EMPATADO!')
elif computador == 0: # COMPUTADOR JOGOU PEDRA 
	if jogador == 1:
		print('Papel vence Pedra! Vitória do Jogador!')
	elif jogador == 2:
		print('Pedra vence Tesoura! Vitória do Computador!')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
	if jogador == 0:
		print('Papel vence Pedra! Vitória do Computador!')
	elif jogador == 2:
		print('Tesoura vence Papel! Vitória do Jogador!')

elif computador == 2: # COMPUTADOR JOGOU TESOURA 
	if jogador == 0:
		print('Pedra vence tesoura! Vitória do Jogador!')
	elif jogador == 1: 
		print('Tesoura vence Papel! Vitória do Computador!')

  




