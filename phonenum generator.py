import random
import time
#choice = list(input("Give me 10 numbers to make a phone number:"))

ch = random.choices((range(0,10)), k = random.randint(10,500))           #first list to start 4loop

def create_phone_number(ch):
    
    firstcouplenums = "".join(str(x) for x in ch[0:3])
    midnums = "".join(str(x) for x in ch[3:6])                      
    last = "".join(str(x) for x in ch[6:10])
    print(f"({firstcouplenums}) {midnums}-{last}")
for i in ch:
    ch = random.choices((range(0,10)), k = random.randint(10,500))    #for the og list to goes thru the loop, makes program unstable in realterminal but vscode terminal shows it perfectly
    time.sleep(0.2)
    create_phone_number(ch)
