
from game_functions import *



num = 'none'
while num != 'anything':
    num = input('Pick a number: ')
    if num == 'exit':
        print('Goodbye')
        break
    num = int(num)
    if div_by_3_and_5(num):
        print('BIZZZZUUUU')
    elif div_by_3(num) :
        print('BIZZ')
    elif div_by_5(num):
        print('ZZUU')
    else:
        print(num)

