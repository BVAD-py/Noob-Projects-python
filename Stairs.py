import math
import random
import time

   
while True:
    
    steps = int(input("How Many Steps In The Stair Case?:"))
    
    if steps == 0:
            break
    
    
    if steps >= 38:
            print("to big to fit standard terminal try less then 38")
            continue
    
    
    for i in range (1,steps+1):
        time.sleep(0.05) 
        print("*" * i)

       