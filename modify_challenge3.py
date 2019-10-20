#!/usr/bin/env python3
import sys
import csv

class Args():
    
    def __init__(self):
        self.args = sys.argv[1:]

    def path_cfg(self):
        try:
            index_c = self.args.index('-c')
        except:
            print("Parameter Error")
            exit(0)
        configfile = self.args[index_c + 1]
        return configfile

    def path_user(self):
        try:
            index_d = self.args.index('-d')
        except:
            print("Parameter Error")
            exit(0)
        userfile = self.args[index_d + 1]
        return userfile

    def path_result(self):
        try:
            index_o = self.args.index('-o')
        except:
            print("Parameter Error")
            exit(0)
        resultfile = self.args[index_o + 1]
        return resultfile

the_args = Args()

class Config():
    
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        config['sum'] = 0
        with open(the_args.path_cfg(), 'r') as file:
            for line in file:
                try:
                    a, b = line.split('=')
                except:
                    print("Parameter Error")
                    exit(0)
                key = a.strip()
                value = float(b.strip())
                if value < 1:
                    config['sum'] += value
                else:
                    config[key] = value
        return config

the_config = Config()

class UserData():
    
    def __init__(self):
        self.userdata = self._read_user_data()

    def _read_user_data(self):
        userdata = []
        with open(the_args.path_user(), 'r') as file:
            data = list(csv.reader(file))
            for i in data:
                try:
                    userdata.append((i[0], int(i[1])))
                except:
                    print("Parameter Error")
                    exit(0)
        return userdata

the_userdata = UserData()

class IncomeTaxCalculator():

    def calc_for_all_userdata(self):
        shebao_rate = the_config._read_config()
        user_data = the_userdata._read_user_data()
        resultlist = []
        for user in user_data:
            if user[1] < shebao_rate['JiShuL']:
                shebao = shebao_rate['JiShuL'] * shebao_rate['sum']
            elif user[1] > shebao_rate['JiShuH']:
                shebao = shebao_rate['JiShuH'] * shebao_rate['sum']
            else:
                shebao = user[1] * shebao_rate['sum']

            money = user[1] - shebao - 5000
            if money <= 0:
                tax = 0
            elif money <= 3000:
                tax = money * 0.03 - 0
            elif money <= 12000:
                tax = money * 0.1 - 210
            elif money <= 25000:
                tax = money * 0.2 - 1410
            elif money <= 35000:
                tax = money * 0.25 - 2660
            elif money <= 55000:
                tax = money * 0.3 - 4410
            elif money <= 80000:
                tax = money * 0.35 - 7160
            else:
            	tax = money * 0.45 - 15160

            income = user[1] - shebao - tax
            resultlist.append((user[0], '{:.2f}'.format(user[1]), '{:.2f}'.format(shebao), '{:.2f}'.format(tax), '{:.2f}'.format(income)))
        return resultlist

    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(the_args.path_result(), 'w') as file:
            writer = csv.writer(file)
            writer.writerows(result)

if __name__ == '__main__':
    cal = IncomeTaxCalculator()    
    cal.export()
