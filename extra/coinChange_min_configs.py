#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'smallestString' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER weight as parameter.
#

import string

def smallestString(weight):
    # Write your code here

    if weight < 0:
        return ''
    # first create the weights map for all the letters
    weights_map = {}
    weights_map['A'] = 1

    coefficient = 3
    letters = string.ascii_uppercase
    for i in range(1, len(letters)):
        weights_map[letters[i]] = coefficient * weights_map[letters[i-1]]
        coefficient += 1

    result = ''
    # minimum number of letters
    # dp[i] = least number of letters to make up weight i
    dp = [weight+1] * (weight+1)
    dp[0] = 0

    weights_map = list(weights_map.items())

    for letter, denom in weights_map[::-1]:
        for i in range(denom, weight+1):
                # simulate taking the letter
                dp[i] = min(dp[i], 1 + dp[i-denom])

    
    # now to build the string having information about how many the fewest number of letters we require

    
    current_weight_ptr = len(weights_map)-1
    
    amount_left = weight
    while amount_left > 0:
        if weights_map[current_weight_ptr][1] <= amount_left:
            amount_left -= weights_map[current_weight_ptr][1]
            result += weights_map[current_weight_ptr][0]
        
        else:
            if current_weight_ptr > 0:
                current_weight_ptr -= 1
            else:
                return -1
    
    return result[::-1]


            
        

    


if __name__ == '__main__':