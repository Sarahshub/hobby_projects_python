# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:59:35 2022

@author: 44791
"""

'''2nd exercise in the python workout book. 
Create a function which sums the content of a list, 
without using the built in sum function '''

def summing_numbers(list_of_numbers):
    sum_of_list = 0
    for i in range(len(list_of_numbers)):
        sum_of_list = sum_of_list + list_of_numbers[i]
    return sum_of_list
 

       
def summing_numbers2(*numbers):
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    print(f'Your sum is {sum_of_numbers}')