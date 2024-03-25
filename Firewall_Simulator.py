#!/bin/python3
import random 

def generate_random_ip():
    return "192.168.0.random.randint{0,100}"
    
blocked_ip =["192.168.0.24","192.168.0.45","192.168.0.32"]
    
for i in range (3):
     if generare_random_ip== blocked_ip[i] :
         print("generate_random_ip and blocked ip are same",generate_random_ip,blocked_ip[i])
         print("IP blocked")
     else:
         print("IP allowed")
         
