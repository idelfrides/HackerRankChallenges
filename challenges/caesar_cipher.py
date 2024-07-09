
'''
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example


The alphabet is rotated by , matching the mapping above. The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Input Format

The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.

Constraints



 is a valid ASCII string without any spaces.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

'''


import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k


def calculate_cipher_position(k: int, current_letter_position: int) -> int:
    alphabet_len = 26
    remainding_len = alphabet_len - current_letter_position
    
    if k <= alphabet_len:
        cipher_posi = k - remainding_len
    else:
        alphabet_len_multile = k//alphabet_len
        remainding_posi = (alphabet_len_multile * alphabet_len) + remainding_len
        
        cipher_posi = k - remainding_posi
        
    return cipher_posi
 

def caesarCipher(s, k):
    
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    
    cipher_text = ''
    
    for letter in s.strip():
        
        print("VERIFYING NUMBERS ... ")
        if letter.isnumeric():
            cipher_text += letter
            continue
        
        print("CHECKING SYMBOLS ... ")
        if letter not in alphabet_lower:
            if letter not in alphabet_upper:
                # that mean it is a symbol
                cipher_text += letter
                continue
            else:
                pass
        
   
        if letter in alphabet_lower:            
            try:
                letter_position = alphabet_lower.index(letter)
                cipher_position = calculate_cipher_position(k, letter_position)
                cipher_text += alphabet_lower[cipher_position]
            except Exception as exc:
                print(f"ERROR ---> {exc}")            
            finally:
                print(f"VARIFICATION DONE FOR LETTER ==>> {letter}")
        
        if letter in alphabet_upper:            
            try:
                letter_position = alphabet_upper.index(letter)
                cipher_position = calculate_cipher_position(k, letter_position)
                cipher_text += alphabet_upper[cipher_position]
            except Exception as exc:
                print(f"ERROR ---> {exc}")            
            finally:
                print(f"VARIFICATION DONE FOR LETTER ==>> {letter}")
        
    
    return cipher_text 



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    range_control = 0
    try:        
        n = int(input("ENTER THE STRING LENGHT in [0, 100] ::>>  ").strip())
        s = input("ENTER THE STRING ::>>  ")
        k = int(input("ENTER THE SHIFT NUMBER in [0, 100] ::>>  ").strip())
    except Exception as exc:
        print(exc)
    else:
        if (n < 0 or n > 100):
            print(f"WARNING: Lenght of the string is out of range -> {n}")
            range_control = 1
        elif (k < 0 or k > 100):
            print(f"WARNING: Lenght of shifts position is out of range -> {k}")
            range_control = 1
            
        if range_control == 1: 
            exit(1)
         
                
    result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()

    print(f"\n THE FINAL RESULT IS:  {result}")
    print("\n\n")    
    