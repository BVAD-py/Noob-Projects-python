import time
import math
print("This is the radius to area calculator")
print("even or odd script runs by final whole number")


while True:
    radius = int(input("raidus: "))
    if radius == 0:
    
        break

    area = math.pi * radius ** 2 

    evef = int(area) % 2 == 0

    if evef is True:
        print("Loading...")      
        time.sleep(3)            
        print(area,"even")
    else:
        print("Loading...")      
        time.sleep(3)
        print(area,"odd")





#import time for interactivity aka time sleep to wait 

#import math for true pi number = better answer



    






