#!/usr/bin/python

import types

"""
Zahlen eingeben, mit q beenden, Mittelwert berechnen
"""

num = []
average = 0


def averageList (myList):
    


if __name__ == "__main__":
    print("Bitte Zahlen eingeben und nach letzter Zahl mit 'q' bestätigen.")
    while True:
        x = input()
        if x == 'q':
            print("letzte Eingabe erfolgt.")
            for i in num:
                average += i
            average /= len(num)
            print(average)

        else:
            try:
                num.append(int(x))
            except:
                print("Falsche Eingabe.")
        