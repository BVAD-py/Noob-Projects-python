import random
import time
import os




print(os.getcwd())

#makes the file exist
file_path = os.path.join(os.path.dirname(__file__),"highscore.txt")

if not os.path.exists(file_path):
    with open(file_path,"w") as file:
        file.write(0)

with open(file_path, "r") as file:
    high_score = int(file.read())
print ("Currect High Score is", high_score)



score = 0

q1 = [
    {"q": "Whats the Capital of Italy", "a": "Rome"},
    {"q": "Whats the Capital of Korea", "a": "Seoul"},
    {"q": "Whats the Capital of Ghana", "a": "Accra"},
    {"q": "Whats the Capital of France", "a": "Paris"},
    {"q": "Whats the Capital of Japan", "a": "Tokyo"},
    {"q": "Whats the Capital of Canada", "a": "Ottawa"},
    {"q": "Whats the Capital of Australia", "a": "Canberra"},
    {"q": "Whats the Capital of Brazil", "a": "Brasilia"},
    {"q": "Whats the Capital of Egypt", "a": "Cairo"},
    {"q": "Whats the Capital of Mexico", "a": "Mexico City"},
    {"q": "Whats the Capital of India", "a": "New Delhi"},
    {"q": "Whats the Capital of China", "a": "Beijing"}
]



def score_system(user_answer1, realanswer1):
    if user_answer1 == realanswer1:
        return + 1
    else:
        return + 0



print("======QUIZ======")
time.sleep(2)

random.shuffle(q1)
for question in q1:
    print(question["q"])

    user_answer1 = input("choose:").lower()    
    realanswer1 = (question["a"].lower())
    sss = score_system(user_answer1, realanswer1) # using sss short way of saying scoresysmtem and blah blah
    score += sss
    time.sleep(0.2)    #reactatibity
    if sss == 1:
        print("Correct your score is", score)
    else:
        print("Wrong your score is", score)
    
    
time.sleep(2)

print("======FINAL SCORE======")

print(score,"/",len(q1))       #for a number out of a number thats fixed if u want to change it time to time make it len(q1)

if score > high_score:
    with open("highscore.txt", "w") as file:
        file.write(str(score))
        print("NEW HIGH SCORE:",score)
else:
    print("nice try but not high score")


for i in range(5):
    print("ending in", i ,"seconds")
    time.sleep(1)