import pandas as pd
from random import *
import time

print("Welcome to my quiz, you are my guess. \n Are you ready to find out if you are a real Erasmus in Warsaw ? 🇵🇱 \n The use of external help is absolutely forbidden (internet, friends..) \n You are ready now, then let's start the game with 10 linguistic questions!")
time.sleep(7)
print("")

df = pd.read_csv("LanguageData.csv", sep=";",encoding='utf-8')
df2 = pd.read_csv("OtherData.csv", sep=";",encoding='utf-8')

count_row_languagedata = df.shape[0]
count_row_otherdata = df2.shape[0]


Sub_category=["Food","Food","Everyday","Politeness","Politeness","Places","Places","Basics","Basics"]

def AskQuestion_SubCategory(i,a):
    df_i= df[df['Sub category'] == i]
    print(f"How do you say '{df_i['Questions'].iloc[a]}' in Polish ?")
    print(f"a) {df_i['A'].iloc[a]}")
    print(f"b) {df_i['B'].iloc[a]}")
    print(f"c) {df_i['C'].iloc[a]}")

def Ask_Other_Question(a, df2):
    print(f"{df2['Questions'].iloc[a]}")
    print(f"a) {df2['A'].iloc[a]}")
    print(f"b) {df2['B'].iloc[a]}")
    print(f"c) {df2['C'].iloc[a]}")

Already_asked_questions=[]
number_of_correct_answer = 0
number_of_the_question = 1

# asking linguistic questions first
for i in Sub_category:
    print(f"----- Question n°{number_of_the_question} // {i} Category")
    time.sleep(1)
    df_i= df[df['Sub category'] == i]
    a = randint(0,df_i.shape[0]-1)
    while a in Already_asked_questions:
        a = randint(0, df_i.shape[0] - 1)
    AskQuestion_SubCategory(i,a)
    answer = input()

    while (answer.lower() != "a") and (answer.lower() != "b") and (answer.lower() != "c"):
        print("You should respond either a, b or c")
        AskQuestion_SubCategory(i,a)
        answer = input()

    if answer.lower()==df_i['Correct answer'].iloc[a]:
        print("\033[32m✔ Well done\033[0m")
        number_of_correct_answer += 1
    else:
        print(f"\033[31m❌ Wrong answer, the correct answer is {df_i['Correct answer'].iloc[a]}\033[0m")

    number_of_the_question+=1
    Already_asked_questions.append(df_i['id'].iloc[a])
    time.sleep(1)
    print(" ")

number_of_correct_linguistic_answers = number_of_correct_answer

loop = 6

#Other type of questions (from other data file)
print("Now, it's time for other types of questions !")
time.sleep(3)

for i in range(loop):
    print(f" \n ----- Question n°{number_of_the_question} // Divers ")
    a = randint(0,count_row_otherdata-1)
    while a in Already_asked_questions:
        a = randint(0, df2.shape[0] - 1)
    Ask_Other_Question(a,df2)
    answer = input()

    while (answer.lower() != "a") and (answer.lower() != "b") and (answer.lower() != "c"):
        print("You should respond either a, b or c")
        Ask_Other_Question(a, df2)
        answer = input()

    if answer.lower()==df2['Correct answer'].iloc[a]:
        print("\033[32m✔ Well done\033[0m")
        number_of_correct_answer += 1
    else:
        print(f"\033[31m❌ Wrong answer, the correct answer is {df2['Correct answer'].iloc[a]}\033[0m")

    number_of_the_question += 1
    Already_asked_questions.append(df2['id'].iloc[a])
    time.sleep(1)
    print("")

number_of_question_asked = number_of_the_question - 1

time.sleep(1)
print(f"The quiz is now finished.")
print("Thank you for your participation !")
time.sleep(2)
print(f"You score is {number_of_correct_answer} out {number_of_question_asked}")
if (number_of_correct_linguistic_answers ==1) or (number_of_correct_linguistic_answers == 0):
    print(f"You had {number_of_correct_linguistic_answers} point out of 10 for the linguistic part")
else :
    print(f"You had {number_of_correct_linguistic_answers} points out of 10 for the linguistic part")

if number_of_correct_answer/number_of_question_asked >= 0.60 :
    print("You are definitely an Erasmus student in Warsaw 🇵🇱‍🎓‍")
elif number_of_correct_answer/number_of_question_asked >= 0.4 :
    print("Are you really an Erasmus student ... ? Well let's say that you missed some of the Polish culture. ")
else:
    print("Well, I don't think that you are an Erasmus student, maybe you are only a tourist in Warsaw ? 📸 \n You should stay a little bit longer in Warsaw !")