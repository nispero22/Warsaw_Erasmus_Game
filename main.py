import pandas as pd
from random import *
import time
import matplotlib.pyplot as plt

print("Welcome to my quizz, you are my guess. \n Are you ready to find out if you are a real Erasmus in Warsaw ? \n The use of external help is absolutely forbidden (internet, friends..) \n You are ready now, then let's start the game ! ")

time.sleep(5)
df = pd.read_csv("OtherData.csv", sep=";")
df2 = pd.read_csv("LanguageData.csv", sep=";")

count_row_otherdata = df.shape[0]
count_row_languagedata = df2.shape[0]

# renvoie la question de la ligne a
def Ask_Other_Question(a,df):
    print(f"{df['Questions'].iloc[a]}")
    print(f"a) {df['A'].iloc[a]}")
    print(f"b) {df['B'].iloc[a]}")
    print(f"c) {df['C'].iloc[a]}")


def Ask_Language_Question(a,df):
    print(f"{df2['Questions'].iloc[a]}")
    print(f"a) {df['A'].iloc[a]}")
    print(f"b) {df['B'].iloc[a]}")
    print(f"c) {df['C'].iloc[a]}")

number_of_correct_answer = 0
loop = 20

# ask 20 questions from other data
for i in range(loop):
    a = randint(0,count_row_otherdata-1)
    Ask_Other_Question(a,df)
    answer = input()

    while (answer.lower() != "a") and (answer.lower() != "b") and (answer.lower() != "c"):
        print("You should respond either a, b or c")
        Ask_Other_Question(a, df)
        answer = input()

    if answer.lower()==df['Correct answer'].iloc[a]:
        print("Well done")
        number_of_correct_answer += 1
    else:
        print(f" Wrong answer, the correct answer is {df['Correct answer'].iloc[a]}")

print(f"The quizz is now finished. Thank you for your try. You score is {number_of_correct_answer} out {loop}")




