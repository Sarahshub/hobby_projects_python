# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:57:44 2022

@author: 44791
"""
from summing_numbers import summing_numbers as sn
from sys import exit

'''Exercise 3 in python workout, 50, 10 min exercises. 
In run timing you should make a function which calculate the avg. 
time a 10 k run takes in minutes. Purpose of exercise is to work with floats 
and converting types. I have added some small things '''

def run_timing():
    print('Let us calculate your avg 10 k run time')
    print('How many runs would you like to include?')
    number_of_user_runs = int(input())
    run_times = []
    if number_of_user_runs == 0:
        exit()
    else:
        for i in range(number_of_user_runs):
            print(f'Please enter {i+1} run in minutes')
            run = float(input())
            run_times.append(run)
        
    total_time = sn(run_times)
    avg_10_k = total_time/len(run_times)
    print(f'Your average 10 k time is: {avg_10_k:.2f}, over {number_of_user_runs} runs')
        
        
    
 