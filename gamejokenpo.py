from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-=-=- Vamos jogar JOKENPO -=-=-')
jogador = int(input('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é a sua jogada: '''))
print('-=' * 15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 20)
sleep(1)
print('O COMPUTADOR ENTROU NA DISPUTA E O JOGADOR ESTÁ PRONTO PARA O DESAFIO!')
print('-=' * 20)
sleep(1)
if computador == jogador: # EMPATE
	print('JOGO EMPATADO! Os dois fizeram a mesma jogada.')
elif computador == 0: # COMPUTADOR JOGOU PEDRA 
	if jogador == 1:
		print('PAPEL VENCE PEDRA! VITÓRIA DO JOGADOR!')
	elif jogador == 2:
		print('PEDRA VENCE TESOURA! VITÓRIA DO COMPUTADOR!')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
	if jogador == 0:
		print('PAPEL VENCE PEDRA! VITÓRIA DO COMPUTADOR!')
	elif jogador == 2:
		print('TESOURA VENCE PAPEL! VITÓRIA DO JOGADOR!')

elif computador == 2: # COMPUTADOR JOGOU TESOURA 
	if jogador == 0:
		print('PEDRA VENCE TESOURA! VITÓRIA DO JOGADOR!')
	elif jogador == 1: 
		print('TESOURA VENCE PAPEL! VITÓRIA DO COMPUTADOR!')

  



  




