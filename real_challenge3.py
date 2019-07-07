#!/usr/bin/env python3
import sys
import csv

class The_Args():
    def __init__(self):
        self.args = sys.argv[1:]

    def operate_args(self, option):
        the_index = self.args.index(option)
        if option == '-c':
            configfile_path = self.args[the_index + 1]
            return configfile_path
        elif option == '-d':
            userdatafile_path = self.args[the_index + 1]
            return userdatafile_path
        elif option == '-o':
            outputfile_path = self.args[the_index + 1]
            return outputfile_path
        else:
            print("Parameter Error")
            exit()

the_args = The_Args()		

class Config():

    def __init__(self):
        self._config = {'Sum':0}
        try:
            with open(the_args.operate_args('-c'), 'r') as f:
                for num in f:
                    a, b = num.split('=')
                    if float(b) > 1:
                        self._config[a.strip()] = float(b.strip())
                    else:
                        self._config['Sum'] += float(b)
        except:
            print("Parameter Error")
            exit(0)

    def get_config(self, the_key):
        return self._config[the_key]

the_config = Config()

class UserData():
    def __init__(self):
        self._userdata = {}
        the_data = []
        try:
            with open(the_args.operate_args('-d'), 'r') as f:
                the_data = list(csv.reader(f))
                for num in the_data:
                    self._userdata[num[0]] = int(num[1])
        except:
            print("Parameter Error")
            exit(0)
        
    def calculator(self):
        self._datas = []
        lower_limmit = the_config.get_config('JiShuL')
        upper_limmit = the_config.get_config('JiShuH')
        sum_rate = the_config.get_config('Sum')
        for ID, salary in self._userdata.items():
            if salary < lower_limmit:
                insure = lower_limmit * sum_rate
            elif salary >= upper_limmit:
            	insure = upper_limmit * sum_rate
            else:
            	insure = salary * sum_rate
            
            income_for_tax = salary - insure - 5000

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
            income = salary - insure - tax
            self._datas.append("{},{:.2f},{:.2f},{:.2f},{:.2f}".format(ID, salary, insure, tax, income))
    
    def dumptofile(self):
        try:
            with open(the_args.operate_args('-o'), 'w') as f:
                for number in range(0,len(self._datas)):
                    f.write(self._datas[number] + "\n")
        except:
            print("Parameter Error")
            exit(0)



if __name__ == '__main__':
    userdata = UserData()
    userdata.calculator()
    userdata.dumptofile()
