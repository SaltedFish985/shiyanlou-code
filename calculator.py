#!/usr/bin/env python3
import sys

try:
    if len(sys.argv) != 2:
        raise ValueError
    salary = int(sys.argv[1])

except:
    print("Parameter Error")
    exit()

income = salary - 5000
if income < 3000:
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
print('{:.2f}'.format(tax))
