#!/bin/python3
import random 
import ipaddress

def generate_random_ip():
    r = random.randint(0, 100)
    addr = ipaddress.ip_address(f"192.168.0.{r}")
    return addr

blocked_ip = ["192.168.0.24", "192.168.0.45", "192.168.0.32"]
print(f"blocked_ip list {blocked_ip}")
    
ip_generated = generate_random_ip()
print("Generated IP:", ip_generated)

# Using a flag to check if the IP is blocked
blocked = False

for blocked_ip_addr in blocked_ip:
    if ip_generated == ipaddress.ip_address(blocked_ip_addr):
        print("IP is blocked:", ip_generated)
        blocked = True
        break

if not blocked:
    print("IP is not blocked:", ip_generated)
