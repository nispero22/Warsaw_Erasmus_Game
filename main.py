import pandas as pd
from random import *
import time

print("Welcome to my quizz, you are my guess. \n Are you ready to find out if you are a real Erasmus in Warsaw ? \n The use of external help is absolutely forbidden (internet, friends..) \n You are ready now, then let's start the game with linguistic questions!")
time.sleep(7)

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

def Ask_Other_Question(a, df):
    print(f"{df['Questions'].iloc[a]}")
    print(f"a) {df['A'].iloc[a]}")
    print(f"b) {df['B'].iloc[a]}")
    print(f"c) {df['C'].iloc[a]}")

Already_asked_questions=[]
number_of_correct_answer = 1
number_of_the_question = 1

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
            print("Well done")
            number_of_correct_answer += 1
    else:
        print(f" Wrong answer, the correct answer is {df['Correct answer'].iloc[a]}")

    number_of_the_question+=1
    Already_asked_questions.append(df_i['id'].iloc[a])
    time.sleep(1)

number_of_correct_lingusitic_answers = number_of_correct_answer


loop = 6

#ask loop number of questions from other data
print("Now, it's time for other types of questions !")
time.sleep(3)
for i in range(loop):
    print(f"----- Question n°{number_of_the_question} // Divers ")
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
        print("Well done")
        number_of_correct_answer += 1
    else:
        print(f" Wrong answer, the correct answer is {df2['Correct answer'].iloc[a]}")

    number_of_the_question += 1
    Already_asked_questions.append(df2['id'].iloc[a])
    time.sleep(1)

number_of_question_asked = number_of_the_question - 1

time.sleep(2)
print(f"The quizz is now finished.")
print("Thank you for your try.")
time.sleep(2)
print(f"You score is {number_of_correct_answer} out {number_of_question_asked}")
if (number_of_correct_lingusitic_answers ==1) or (number_of_correct_lingusitic_answers == 0):
    print(f"You had {number_of_correct_lingusitic_answers} point out of {number_of_question_asked} for lingusitic part")
else :
    print(f"You had {number_of_correct_lingusitic_answers} points out of {number_of_question_asked} for lingusitic part")

if number_of_correct_answer/number_of_question_asked >= 0.60 :
    print("You are definetely an Erasmus student in Warsaw")
elif number_of_correct_answer/number_of_question_asked >= 0.4 :
    print("Are you really an Erasmus student ? Well let's say that you missed some of the Polish culture. ")
else:
    print("Well, I don't think that you are an Erasmus student, maybe you are only a tourist in Warsaw ? Let's stay a little bit longer in Warsaw !")

