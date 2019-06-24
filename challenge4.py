#!/usr/bin/env python3
import sys
import csv
from multiprocessing import Process, Queue

queue1 = Queue()
queue2 = Queue()

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

args = sys.argv[1:]
configfile = args[args.index('-c') + 1]
myconfig = Config(configfile)

class UserData(Process):
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def read_users_data(self, q):
        userlist = {}
        the_data = []
        try:
            with open(args[args.index('-d') + 1], 'r') as f:
                the_data = list(csv.reader(f))
                for num in the_data:
                    userlist[num[0]] = num[1]
        except:
            print("Parameter Error")
            exit()
        q.put(userlist)

    def calculator(self, q1, q2):
        try:
            userdata = q1.get(timeout=2)
        except queque.Empty:
            exit()
        datas = []
        lower_limmit = float(myconfig.get_config()['JiShuL'])
        upper_limmit = float(myconfig.get_config()['JiShuH'])
        yang_lao = float(myconfig.get_config()['YangLao'])
        yi_liao = float(myconfig.get_config()['YiLiao'])
        shi_ye = float(myconfig.get_config()['ShiYe'])
        gong_shang = float(myconfig.get_config()['GongShang'])
        sheng_yu = float(myconfig.get_config()['ShengYu'])
        gong_ji_jin = float(myconfig.get_config()['GongJiJin'])
        for ID, salary in userdata.items():
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
            datas.append("{},{:.2f},{:.2f},{:.2f},{:.2f}".format(ID, float(salary), insure, tax, income))
        q2.put(datas)
    
    def dumptofile(self,q):                
        try:
            datas = q.get(timeout=3)    
            with open(args[args.index('-o') + 1], 'w') as f:
                for number in range(0,len(datas)):
                    f.write(datas[number] + "\n")
        except queque.Empty:
            exit()
        
        except IndexError:
            print("Parameter Error")
            exit()
            
def process():
    userdata = UserData(queue1, queue2)
    p1 = Process(target=userdata.read_users_data, args=(queue1, ))
    p2 = Process(target=userdata.calculator, args=(queue1, queue2))
    p3 = Process(target=userdata.dumptofile, args=(queue2, ))
    p1.start()
    p2.start()
    p3.start()


if __name__ == '__main__':   
    process()



