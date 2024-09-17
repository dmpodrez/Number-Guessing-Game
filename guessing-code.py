import random 
from_num = int(input())
to_num = int(input())
num = 0

def random_num(from_num, to_num):
  number = random.randint(from_num, to_num)
  return number

def guess(key_num):
  count = 0 
  while True:
    n = int(input())
    print('Your number:', n) 
    if n > key_num:
      print('Too much, try again')
      count += 1
    elif n < key_num:
      print('Too few, try again')
      count += 1
    else:
      print('You guessed, congratulations!')
      print('You guessed the number in', count, 'attempts')
      break
  print('Do you want to play one more time?')
  another_game = input()
  if another_game.lower() == 'yes':
    key_num = random_num(from_num, to_num)
    guess(key_num)
  else:
    print('Thanks for the game')

key_num = random_num(from_num, to_num)
guess(key_num)
