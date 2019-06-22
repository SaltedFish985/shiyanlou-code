#!/usr/bin/env python3
import socket
import sys
import re

def operate_argv(the_argv, option):
    try:
        index = the_argv.index(option)
        return the_argv[index + 1]
    except (ValueError, IndexError):
    	print("Parameter Error")
    	exit()

def socket_con(the_ip, the_port):
    s = socket.socket()
    s.settimeout(0.1)
    try:
        s.connect((the_ip, int(the_port)))
        print('{} open'.format(the_port))
    except ConnectionRefusedError:
        print('{} closed'.format(the_port))
    finally:
        s.close()

def operate_port(ports):
    if re.findall('\d-\d', ports) != []:
        start_port, end_port = ports.split('-')
        return (int(start_port), int(end_port))
    else:
        return ports

def the_main():
    the_ip = operate_argv(sys.argv[1:], '--host')
    if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', the_ip) == []:
    	print("Parameter Error")
    	exit()
    the_port = operate_argv(sys.argv[1:], '--port')
    real_port = operate_port(the_port)
    if isinstance(real_port, tuple):
        for one_port in range(real_port[0], real_port[1]+1):
            socket_con(the_ip, one_port)
    else:
        socket_con(the_ip, real_port)

if __name__ == '__main__':
    the_main()