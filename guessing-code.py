import random 
def guess(key_num):
  while True:
    n = int(input())
    print('Your number:', n) 
    if n > key_num:
      print('Too much, try again')
    elif n < key_num:
      print('Too few, try again')
    else:
      print('You guessed, congratulations!')
      break

from_num = int(input())
to_num = int(input())
key_num = random.randint(from_num, to_num) 

print(guess(key_num))
