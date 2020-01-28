#!/usr/bin/python

import types

"""
Zahlen eingeben, mit q beenden, Mittelwert berechnen
"""

num = []



def averageList (myList):
    average = 0
    for i in myList:
        average += i
    average /= len(myList)
    return average


def appendToList (x):
    if x == 'q':
        print("Letzte Eingabe erfolgt.")
        print(averageList(num))
        exit()
    else:
        try:
            num.append(int(x))
        except:
            print("Falsche Eingabe.")
    


if __name__ == "__main__":
    print("Bitte Zahlen eingeben und nach letzter Zahl mit 'q' bestätigen.")
    while True:
        appendToList(input())

        
        