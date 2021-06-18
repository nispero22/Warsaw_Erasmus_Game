import pandas as pd
from random import *
import time
import matplotlib.pyplot as plt

#print("Welcome to my quizz, you are my guess. \n Are you ready to find out if you are a real Erasmus in Warsaw ? \n The use of external help is absolutely forbidden (internet, friends..) \n You are ready now, then let's start the game ! ")
#time.sleep(5)

df = pd.read_csv("LanguageData.csv", sep=";", encoding='utf-8')
print(df['A'].iloc[134])
print("piątek")

def AskQuestion_SubCategory(i,a):
    df_i= df[df['Sub category'] == i]
    print(f"How do you say '{df_i['Questions'].iloc[a]}' in Polish ?")
    print(f"a) {df_i['A'].iloc[a]}")
    print(f"b) {df_i['B'].iloc[a]}")
    print(f"c) {df_i['C'].iloc[a]}")

Sub_category=["Food","Food","Everyday","Everyday","Politeness","Politeness","Places","Places","Basis","Basis"]
Already_asked_questions = []
number_of_correct_answer = 0
number_of_question_asked = 1


for i in Sub_category:
    print(f"Question n°{number_of_question_asked} // {i} Category")
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

    number_of_question_asked+=1
    Already_asked_questions += df_i['id'].iloc[a]
    time.sleep(1)






