import random
import time
import os

score = 0

q1 = [
    {"q1": "Whats the Capital of Italy", "a": "Rome"},
    {"q1": "Whats the Capital of Korea", "a": "Seoul"},
    {"q1": "Whats the Capital of Ghana", "a": "Accra"},
    {"q1": "Whats the Capital of France", "a": "Paris"},
    {"q1": "Whats the Capital of Japan", "a": "Tokyo"},
    {"q1": "Whats the Capital of Canada", "a": "Ottawa"},
    {"q1": "Whats the Capital of Australia", "a": "Canberra"},
    {"q1": "Whats the Capital of Brazil", "a": "Brasilia"},
    {"q1": "Whats the Capital of Egypt", "a": "Cairo"},
    {"q1": "Whats the Capital of Mexico", "a": "Mexico City"},
    {"q1": "Whats the Capital of India", "a": "New Delhi"},
    {"q1": "Whats the Capital of China", "a": "Beijing"}
]

q2 = [
    {"q": "What is 2 + 2?", "a": "4"},
    {"q": "What is 5 × 3?", "a": "15"},
    {"q": "What is 10 - 7?", "a": "3"},
    {"q": "What is 9 ÷ 3?", "a": "3"},
    {"q": "What is 6 + 8?", "a": "14"},
    {"q": "What is 12 × 2?", "a": "24"},
    {"q": "What is 20 - 5?", "a": "15"},
    {"q": "What is 7 × 7?", "a": "49"},
    {"q": "What is 18 ÷ 2?", "a": "9"},
    {"q": "What is 15 + 10?", "a": "25"},
    {"q": "What is 100 ÷ 10?", "a": "10"},
    {"q": "What is 11 × 3?", "a": "33"}
]

print("======QUIZ======")
time.sleep(2)

print("1 - Country Capital Quiz")
print("2 - Math Quiz")
quizchoice = input("Choose:")

print(os.getcwd())

#makes the file exist
file_path1 = os.path.join(os.path.dirname(__file__),"highscore.txt")
file_path2 = os.path.join(os.path.dirname(__file__),"highscore2.txt")

if quizchoice == "1":
    file_path = file_path1
elif quizchoice == "2":
    file_path = file_path2
else:
    "404 high score failure, pick a real quiz"
    exit()

if not os.path.exists(file_path):
    with open(file_path,"w") as file:
        file.write("0")

with open(file_path, "r") as file:
    high_score = int(file.read())
print ("======Currect High Score is", high_score,"======")

def score_system(user_answer1, realanswer1):
    if user_answer1 == realanswer1:
        return  1
    else:
        return  0



random.shuffle(q1)
random.shuffle(q2)



if quizchoice == "1":
    for question in q1:
            print(question["q1"])

            user_answer1 = input("choose:").lower()    
            realanswer1 = (question["a"].lower())
            sss = score_system(user_answer1, realanswer1) # using sss short way of saying scoresysmtem and blah blah
            score += sss
            time.sleep(0.2)    #reactatibity
            if sss == 1:
                print("Correct your score is", score)
            else:
                print("Wrong your score is", score)

if quizchoice == "2":
    for question in q2:
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

print(score,"/12")       #for a number out of a number thats fixed if u want to change it time to time make it len(q1)

if score > high_score:
    with open(file_path, "w") as file:
        file.write(str(score))
        print("NEW HIGH SCORE:",score)
else:
    print("nice try but not high score")


for i in range(5):
    print("ending in", i ,"seconds")
    time.sleep(1)