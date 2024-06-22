#!bin/env/python3

import math
import os
import numpy
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    #  n --> number of towers
    #  m --> higth of each tower
    
    player_one , player_two = 1, 2
    
    round_of_game = 0
    
    while True:
        round_of_game += 1
        player_ref = round_of_game
        
        tower_reference = random.randint(1, n)
        choice_reduce = random.randint(1, m-1)
        # _reduce = random.randint(1, m-1)
        
        
        print(choice_reduce)
        print(tower_reference)
        
    return 0

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input("ENTER TEST CASES QUANTITY  ::>>  ").strip())

    for t_itr in range(t):
        first_multiple_input = input("ENTER n and m VALUES [eg.: 2 4] ::>>  ").rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)
        
        print(f'THE RESULT IS  >>>>>>  {result}')


        # fptr.write(str(result) + '\n')

    # fptr.close()
