#!/bin/env/python3

import math
import os
import random
import re
import sys
# from dotenv import load_dotenv

from LIBS import manager as man
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


    
def gridChallenge(grid):
    
    # WARNING: test case 10 still showing an error. I do not know how to fix it.
     
    if len(grid) == 1:
        return "YES"
    
    grid_help_tuple = tuple(grid)
    grid_help_list = list()
    grid_sorted = list()

    for item in grid_help_tuple:
        sorted_item = man.order_string(item)
        grid_help_list.append(sorted_item)
        
    row_control = 0
    col_string = ''
    col_control = 0
    break_while = False
    col_asc_ordered = "YES"
    
    while True:        
        col_string += grid_help_list[row_control][col_control]
        if row_control == len(grid) - 1:    
            col_string_sorted = man.verify_column_letters(col_string)
            if col_string != col_string_sorted:
                col_asc_ordered = "NO"
                break_while = True
            else:
                col_string = ''
            
            row_control = 0
            col_control += 1
        else:
            row_control += 1
            
        if break_while or (col_control == (len(grid) - 1)):
            break
                    

    return  col_asc_ordered

  
def run_grid_challenge_via_terminal():

    t = int(input("ENTER THE NUMBER OF TESTCASES in [0, 100] ::>>  ").strip())

    for t_itr in range(t):
        print(f"TESTCASE NUMBER ---> [{t_itr + 1}]\n\n")
        
        n = int(input("ENTER THE LENGHT OF GRID in [0, 100] ::>>  ").strip())

        grid = []

        for row in range(n):
            print(f"FILL OUT CONTENT FOR ROW = {row + 1}")
            grid_item = input(f"ENTER THE SEQUENCE OF {n} CHARACTERES ::>>  ")
            grid.append(grid_item)

        result = gridChallenge(grid)
 
        print(f"\n THE FINAL RESULT FOR TESTCASE [{t_itr + 1}] IS: \n\n  {result}")
        print("\n\n") 
        print('#'*80)
        

def run_grid_challenge_through_files():
   
    filepath = man.build_file_full_path("input_file.txt")    
    data = man.read_files(filepath, "r")
  
    data = data.split('\n')
    data.pop(-1)   
    test_cases = eval(data.pop(0))
    
    filepath = man.build_file_full_path("output_file.txt")    
    fptr = open(filepath, "w")
    
    for tc_itr in range(test_cases):
        if tc_itr == 74:
            import pdb
            pdb.set_trace()
            
        print(f"\n\tTESTCASE NUMBER ---> [{tc_itr + 1}]")
        
        grid_size = eval(data.pop(0))
        grid = data[:grid_size]
        del data[:grid_size]

        result = gridChallenge(grid)

        fptr.write(result + '\n')    
    
        print(f"\n\tFINAL RESULT FOR TESTCASE [{tc_itr + 1}] IS: {result}")
        print("\n") 
        print('#'*80)
        
    fptr.close()
    return
