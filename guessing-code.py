import random 
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

from_num = int(input())
to_num = int(input())
key_num = random.randint(from_num, to_num) 

guess(key_num)
