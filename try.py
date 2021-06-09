import pandas as pd
from random import *
import matplotlib.pyplot as plt

df = pd.read_csv("test.csv",sep=";")
count_row = df.shape[0]

# renvoie la question de la ligne a
def AskQuestion(a,df):
    print(f"{df['Questions'].iloc[a]}")
    print(f"a) {df['A'].iloc[a]}")
    print(f"b) {df['B'].iloc[a]}")
    print(f"c) {df['C'].iloc[a]}")


# pose 20 questions
for i in range(3):
    a = randint(0,count_row-1)
    AskQuestion(a,df)
    answer = input()

    while (answer.lower() != "a") and (answer.lower() != "b") and (answer.lower() != "c"):
        print("You should respond either a, b or c")
        AskQuestion(a, df)
        answer = input()

    if answer.lower()==df['Correct answer'].iloc[a]:
        print("Well done")
    else:
        print(f" Wrong answer, the correct answer is {df['Correct answer'].iloc[a]}")




