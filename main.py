# Okay
# i no where i go start like this buh..........
import random
from tkinter import *

import time

A1 = 6
B2 = 5
B3 = 4
C4 = 3
C5 = 2
C6 = 1


def generate_code():

    code = random.randrange(113, 201)

    return code


def run_calc():
    sub_list = []

    Sub_Dict = {

        101: 'English Language',
        102: "Mathematics",
        103: 'Further Mathematics',
        104: 'Physics',
        105: 'Chemistry',
        106: 'Biology',
        107: 'Geography',
        108: 'Economics',
        109: 'Government',
        110: 'Accounts',
        111: 'CRS',
        112: 'Commerce',
    }

    Sub_Dict2 = {

    }

    # sub_list2 = []

    Grade_Dict = {

        'A1': 6,
        'B2': 5,
        'B3': 4,
        'C4': 3,
        'C5': 2,
        'C6': 1
    }

    Grade_Dict2 = {


    }
    Grade_list = []

    print()

    for k, v in Sub_Dict.items():
        sub_list.append(k)
        print(k, ':', v)

    print('\nNote if subject not in the list above,Enter any digit')

    for i in range(5):

        Sub_code = int(input("Enter Subject Code from the above : "))
        print("Validating Code")
        time.sleep(4)
        if Sub_code in sub_list:
            sub_fin = Sub_Dict[Sub_code]
            sub_grade = input("Enter grade for " + sub_fin + ':')
            Sub_Dict2[sub_fin] = sub_grade
            print('\n')

            sub_fin2 = Grade_Dict[sub_grade]

            Grade_Dict2[sub_grade] = sub_fin2

            Grade_list.append(sub_fin2)
            # print(Grade_list)
            summer = sum(Grade_list)

        elif Sub_code not in sub_list:
            sub = input("Enter Subject: ")
            sub_list.append(Sub_code)
            generate_code()
            Sub_Dict[generate_code()] = sub
            print(Sub_Dict)

            # sub_fin3 = Sub_Dict[Sub_code]
            sub_grade = input("Enter grade for " + sub + ':')
            Sub_Dict2[sub] = sub_grade
            print('\n')

            sub_fin4 = Grade_Dict[sub_grade]

            Grade_Dict2[sub_grade] = sub_fin4

            Grade_list.append(sub_fin4)
            # print(Grade_list)
            summer = sum(Grade_list)

    return summer


# print(generate_code())
# Run_Calc()


def origin():

    print("WElCOME  HOME")

    sittings = int(input("Enter your numbers of sittings(1 / 2) : ")).capitalize()
    if sittings == 1:
        score = run_calc()
        score += 10
        UTME_SCORE = int(input("Enter your UTME Score: "))
        UTME_POINT = (UTME_SCORE/400) * 60
        FINAL_POINT = UTME_POINT + score

        print("Your Screening Point:  ", FINAL_POINT)

    elif sittings == 2:
        term = run_calc()
        term += 6

        UTME_SCORE = int(input("Enter your UTME Score: "))
        UTME_POINT = (UTME_SCORE / 400) * 60
        FINAL_POINT = UTME_POINT + term

        print("Your Screening Point:  ", FINAL_POINT)


origin()
