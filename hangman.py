'''
This is a simple hangman game.

'''

import random
from words import word_list

print('\n')
print('Welcome to hangman.\n')
print('You have 6 lives to guess the word \n')
print('if you guess wrong then you will lose your 1 live \n')


lives = 6
com_choice = list(random.choice(word_list).upper())
length_word = ['_' for _ in com_choice]

print('Guess word: ',length_word)




while True:  
  if '_' not in length_word:
                  print('Congratulation You guessed the correct word: ',' '.join((length_word)))
                  break
  
  user = input('guess a letter: ').upper()  

  if user not in com_choice:
      print('you guessed wrong')
      lives -= 1
      print('Current lives :',lives)
      if lives == 0:
          print('Game over , you lose.')
          print('Correct word:',' '.join(com_choice))
          break
      continue

  for i in range(len(com_choice)):
          if user == com_choice[i]:
              length_word[i] = user
              print('Right guess')
              print(' '.join((length_word)))
              continue
  
  
     

    

