import random

#simplificações
win = ('Ganhas-te!')
lose = ('Perdes-te!')

#defenidor de rondas
while True:
 numero = int(input('Quantas rondas queres jogar? - '))
 if (numero%2 == 0):
  print('Presisa ser uma número impar!\n')
 if (numero%2 != 0):
  print(f'Então vamos jogar {numero:d} rondas.\n')
  break

#valores de jogo
rondas = numero
user_1 = 0
user_2 = 0



#jogo em loop
while True:         
     u_c = input('Pedra, papel ou tesoura? - ')
     c = ('pedra', 'papel', 'tesoura')
     pc_c = random.choice(c)
     print(f'\nTu escolhes-te {u_c.lower():s} e o computador escolheu {pc_c:s}.')
     #variaveis de jogo
     if u_c.lower() == pc_c:
               print(f'O jogo empatou.')
     elif u_c.lower() == 'pedra':
          if pc_c == 'papel':
               print(lose)
               user_2 = user_2+1
          else:
               print(win)
               user_1=user_1+1
     elif u_c.lower() == 'papel':
          if pc_c == 'tesoura':
               print(lose)
               user_2 = user_2+1
          else:
               print(win)
               user_1=user_1+1
     elif u_c.lower() == 'tesoura':
          if pc_c == 'pedra':
               print(lose)
               user_2 = user_2+1
          else:
               print(win)
               user_1=user_1+1
     print('Utilizador - ', user_1)
     print('Computador - ', user_2)
     
     #calculo de fim de jogo
     if (user_1 or user_2) > rondas/2 or (user_1+user_2 == rondas):
          if user_1 > user_2:
               print(f'\nTu ganhas-te com {user_1:d} de {rondas:d} pontos!')
          else:
               print(f'\nTu perdes-te com {user_1:d} de {rondas:d} pontos!\n')
          (user_1, user_2) = (0, 0)
          #Creditos
          print('Este jogo foi feito por Levadas-CODE e uma agradecimento especial a SL4SH!')
          #repetição de jogo
          repetir = input("\nRepetir? (s/n) - ")
          if repetir.lower() != "s":
               break
              
              
'''Todos os créditos vão para Levadas-CODE e um agradecimento especial para SL4SH.'''