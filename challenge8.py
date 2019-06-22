# -*- coding: utf-8 -*-

import re 
from datetime import datetime
from collections import Counter

def open_parser(filename):
    with open(filename) as logfile:
        
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s' 
                   r'\[(.+)\]\s'  
                   r'"GET\s(.+)\s\w+/.+"\s'  
                   r'(\d+)\s'  
                   r'(\d+)\s'  
                   r'"(.+)"\s'  
                   r'"(.+)"'  
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    ips = []
    urls = []
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    for log in logs:
        if(re.findall('11/Jan/2017', log[1]) != []):
            # ips.append(re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', log[0])[0])
            ips.append(log[0])
        if(int(log[3]) == 404):
            # urls.append(re.findall('\s.+\s', log[2])[0].strip())
            urls.append(log[2])
    ipc = Counter(ips)
    urlc = Counter(urls)
    ip_dict = dict(tuple(ipc.most_common(1)))
    url_dict = dict(tuple(urlc.most_common(1)))
    return ip_dict, url_dict
    


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)

    
    
