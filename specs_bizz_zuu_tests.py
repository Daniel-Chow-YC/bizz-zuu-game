from game_functions import *

print('Testing div_by_3 with 3, expected True')
print(div_by_3(3) == True)
print('Testing div_by_3 with 5, expect True')
print(div_by_3(5) == False)
# We are going to do tdd
print('Testing div_by_5 with 5, expect True')
print(div_by_5(5) == True)
print('Testing div_by_5 with 6, expect True')
print(div_by_5(6) == False)
# Check if divisible by 3 and 5
print('div_by_3_and_5 expect True')
print(div_by_3_and_5(15) == True)