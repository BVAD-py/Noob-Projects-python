import time

while True:
    print("1. Even/Odd")
    print("2. Square/Cube")
    print("0. Exit")

    choice = input("Choose: ")
    
    if choice == "0":
        break

    if choice == "1":
       while True:
        time.sleep(0.25)
        ch1num =  int(input("Choose Number: "))
        if ch1num == 0:
            break
        if ch1num % 2 == 0:
            print("This Number Is Even ")
        else: 
            print("This Number Is Odd ")
    
        time.sleep(2)
        if ch1num == 0:
            break

    if choice == "2":
        while True:
           time.sleep(0.25)
           ch2num = int(input("1 for squared Or 2 for cubed "))
           if ch2num == 1:
            cubicnum = int(input("pick a whole number: "))
            print(cubicnum ** 2)
            time.sleep(2)

            break

           else:
              if ch2num == 2:
                 cubinum = int(input("pick a whole number   "))
                 print(cubinum ** 3)

                 time.sleep(2)

                 break

    if choice != ("0,1,2"):
       print("press an real button ")
       continue
    

    

 







