#!/usr/bin/env python3
import sys
import csv
import getopt
from configparser import ConfigParser
from multiprocessing import Process, Queue
from datetime import datetime

class The_Args():
    def __init__(self):
        self.myargs = sys.argv[1:]
        self.cityname = ''
        self.Configfile = ''
        self.userdata = ''
        self.resultdata = ''
        try:
            opts,args = getopt.getopt(self.myargs, "hC:c:d:o:", ["help"])
        except getopt.GetoptError:
            print("Parameter Error")
            exit()
        for opt, arg in opts:
            if opt == ("-h", "--help"):
                print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
                exit()
            elif opt == "-C":
                self.cityname = arg
            elif opt == "-c":
                self.Configfile = arg
            elif opt == "-d":
                self.userdata = arg
            elif opt == "-o":
                self.resultdata = arg

the_args = The_Args()

queue1 = Queue()
queue2 = Queue()

class Config():

    def __init__(self):
        self.hconfig = {}
        city = the_args.cityname.upper()
        myconfig = ConfigParser()
        myconfig.read(the_args.Configfile)
        list_header = myconfig.sections()
        if city in list_header:
            for num in myconfig.items(city):
                a, b = num
                self.hconfig[a.strip()] = b.strip()
        else:
            for num in myconfig.items("DEFAULT"):
                a, b = num
                self.hconfig[a.strip()] = b.strip()
    
    def get_config(self):
        return self.hconfig     

the_config = Config()

class UserData(Process):
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def read_users_data(self, q):
        Newuserlist = {}
        the_data = []
        try:
            with open(the_args.userdata, 'r') as f:
                the_data = list(csv.reader(f))
                for num in the_data:
                    Newuserlist[num[0]] = num[1]
        except:
            print("Parameter Error")
            exit()
        q.put(Newuserlist)

    def calculator(self, q1, q2):        
        try:
            Newuserdata = q1.get(timeout=3)
        except queque.Empty:
            exit()
        datas = []
        lower_limmit = float(the_config.get_config()['jishul'])
        upper_limmit = float(the_config.get_config()['jishuh'])
        yang_lao = float(the_config.get_config()['yanglao'])
        yi_liao = float(the_config.get_config()['yiliao'])
        shi_ye = float(the_config.get_config()['shiye'])
        gong_shang = float(the_config.get_config()['gongshang'])
        sheng_yu = float(the_config.get_config()['shengyu'])
        gong_ji_jin = float(the_config.get_config()['gongjijin'])
        for ID, salary in Newuserdata.items():
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
            the_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            datas.append("{},{:.2f},{:.2f},{:.2f},{:.2f},{}".format(ID, float(salary), insure, tax, income, the_time))
        q2.put(datas)
    
    def dumptofile(self,q):                
        try:
            Newdatas = q.get(timeout=3)    
            with open(the_args.resultdata, 'w') as f:
                for number in range(0,len(Newdatas)):
                    f.write(Newdatas[number] + "\n")
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



