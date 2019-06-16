#!/usr/bin/env python3
import sys
import csv

class Config():

    def __init__(self, configfile):
        self._config = {}
        try:
            with open(configfile, 'r') as f:
                for num in f:
                    a, b = num.split('=')
                    self._config[a.strip()] = b.strip()
        except:
            print("Parameter Error")
            exit(0)

    def get_config(self):
        return self._config

class UserData():
    def __init__(self, userdatafile):
        self._userdata = {}
        the_data = []
        try:
            with open(userdatafile, 'r') as f:
                the_data = list(csv.reader(f))
                for num in the_data:
                    self._userdata[num[0]] = num[1]
        except:
            print("Parameter Error")
            exit(0)

    def calculator(self,configdict):
        self._datas = []
        lower_limmit = float(configdict['JiShuL'])
        upper_limmit = float(configdict['JiShuH'])
        yang_lao = float(configdict['YangLao'])
        yi_liao = float(configdict['YiLiao'])
        shi_ye = float(configdict['ShiYe'])
        gong_shang = float(configdict['GongShang'])
        sheng_yu = float(configdict['ShengYu'])
        gong_ji_jin = float(configdict['GongJiJin'])
        for ID, salary in self._userdata.items():
            if int(salary) < lower_limmit:
                insure = lower_limmit * (yang_lao + yi_liao + shi_ye + gong_shang + sheng_yu + gong_ji_jin)
            elif int(salary) >= upper_limmit:
            	insure = upper_limmit * (yang_lao + yi_liao + shi_ye + gong_shang + sheng_yu + gong_ji_jin)
            else:
            	insure = int(salary) * (yang_lao + yi_liao + shi_ye + gong_shang + sheng_yu + gong_ji_jin)
            
            income_for_tax = int(salary) - insure - 5000

            if income_for_tax < 0:
                income_for_tax = 0
                rate = 0
                qcd = 0
            elif income_for_tax >=0 and income_for_tax < 3000:
                rate = 0.03
                qcd = 0
            elif income_for_tax >=3000 and income_for_tax < 12000:
                rate = 0.1
                qcd = 210
            elif income_for_tax >=12000 and income_for_tax < 25000:
                rate = 0.2
                qcd = 1410
            elif income_for_tax >= 25000 and income_for_tax < 35000:
                rate = 0.25
                qcd = 2660
            elif income_for_tax >= 35000 and income_for_tax < 55000:
                rate = 0.3
                qcd = 4410
            elif income_for_tax >= 55000 and income_for_tax < 80000:
                rate = 0.35
                qcd = 7160
            elif income_for_tax >= 80000:
                rate = 0.45
                qcd = 15160

            tax = income_for_tax * rate - qcd
            income = int(salary) - insure - tax
            self._datas.append("{},{:.2f},{:.2f},{:.2f},{:.2f}".format(ID, float(salary), insure, tax, income))
    
    def dumptofile(self, outputfile):
        try:
            with open(outputfile, 'w') as f:
                for number in range(0,len(self._datas)):
                    f.write(self._datas[number] + "\n")
        except:
            print("Parameter Error")
            exit(0)



if __name__ == '__main__':
    args = sys.argv[1:]
    configfile = args[args.index('-c') + 1]
    userdatafile = args[args.index('-d') + 1]
    outputfile = args[args.index('-o') + 1]
    myconfig = Config(configfile)
    userdata = UserData(userdatafile)
    userdata.calculator(myconfig.get_config())
    userdata.dumptofile(outputfile)


