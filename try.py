import pandas as pd
from random import *
import matplotlib.pyplot as plt

print("Welcome to my quizz, you are my guess. \n Are you ready to find out if you are a real Erasmus in Warsaw ? \n The use of external help is absolutely forbidden (internet, friends..) \n You are ready now, then let's start the game ! ")

df = pd.read_csv("Data.csv", sep=";")
count_row = df.shape[0]

# renvoie la question de la ligne a
def AskQuestion(a,df):
    print(f"{df['Questions'].iloc[a]}")
    print(f"a) {df['A'].iloc[a]}")
    print(f"b) {df['B'].iloc[a]}")
    print(f"c) {df['C'].iloc[a]}")


number_of_correct_answer = 0
loop = 20

# ask 20 questions
for i in range(loop):
    a = randint(0,count_row-1)
    AskQuestion(a,df)
    answer = input()

    while (answer.lower() != "a") and (answer.lower() != "b") and (answer.lower() != "c"):
        print("You should respond either a, b or c")
        AskQuestion(a, df)
        answer = input()

    if answer.lower()==df['Correct answer'].iloc[a]:
        print("Well done")
        number_of_correct_answer += 1
    else:
        print(f" Wrong answer, the correct answer is {df['Correct answer'].iloc[a]}")

print(f"The quizz is now finished. Thank you for your try. You score is {number_of_correct_answer} out {loop}")




