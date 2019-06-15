#!/usr/bin/env python3
import sys

def calculate_money(salary):
    income = salary * (1-0.165) - 5000
    if income < 0:
        rate = 0
        qcd = 0
    elif income >=0 and income < 3000:
        rate = 0.03
        qcd = 0
    elif income >=3000 and income < 12000:
        rate = 0.1
        qcd = 210
    elif income >=12000 and income < 25000:
        rate = 0.2
        qcd = 1410
    elif income >= 25000 and income < 35000:
        rate = 0.25
        qcd = 2660
    elif income >= 35000 and income < 55000:
        rate = 0.3
        qcd = 4410
    elif income >= 55000 and income < 80000:
        rate = 0.35
        qcd = 7160
    elif income >= 80000:
        rate = 0.45
        qcd = 15160

    tax = income * rate - qcd
    money = salary * (1-0.165) - tax
    return money
    
if __name__ == '__main__':
    moneys = {}
    try:
        if len(sys.argv) < 2:
            raise ValueError
        for str_ in sys.argv[1:]:
            a, b = str_.split(':')
            moneys[a] = calculate_money(int(b))

    except:
        print("Parameter Error")
        exit()

    for key, value in moneys.items():
        print("{}:{:.2f}".format(key, value))