__author__ = "Richard O'Dwyer"
__email__ = "richard@richard.do"
__license__ = "None"
#--------------------
__edited_by__ = 'B lugo'

import re
from operator import itemgetter

def process_log(log):
    requests = get_requests(log)
    files = get_files(requests)
    totals = file_occur(files)
    list_1 = []
    un = []
    print(files,"here i am")
    for i in requests:
        if i[3] == '200':
            ni2 = [i[0], i[3]]
            un.append(ni2)
        #print(i)
        print(i[0])
        ni = i[0]
        list_1.append(ni)
    print(un,'YOOOOOOOOO')
    res2 = [] 
    for i in un:
        print(i)
        if i[0] not in res2:
            ni3 = [i[0], i[1]]
            res2.append(ni3)
    print('GOOOOOO',res2,"GOTCHAAAAAA")
    res = [] 
    for i in list_1: 
        if i not in res: 
            res.append(i)
    x = len(list_1)
    x1 = len(res)
    print("count list1",x)
    print("count after",x1)
    print(res)
    return list_1

def get_requests(f):
    log_line = f.read()
    pat = (r''
           '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP address
           '\[(.+)\]\s' #datetime
           '"GET\s(.+)\s\w+/.+"\s' #requested file
           '(\d+)\s' #status
           '(\d+)\s' #bandwidth
           '"(.+)"\s' #referrer
           '"(.+)"' #user agent
        )
    requests = find(pat, log_line)
    return requests

def find(pat, text):
    match = re.findall(pat, text)
    if match:
        return match
    return False

def get_files(requests):
    #get requested files with req
    requested_files = []
    for req in requests:
        # req[2] for req file match, change to
        # data you want to count totals
        requested_files.append(req[2])
    return requested_files

def file_occur(files):
    # file occurrences in requested files
    d = {}
    for file in files:
        d[file] = d.get(file,0)+1
    return d

if __name__ == '__main__':

    #nginx access log, standard format
    log_file = open('access.log', 'r')
    ####print(log_file.readline(),'WOOOOOOOOOOOOOOOOOOOOo')

    # return dict of files and total requests
    urls_with_counts = process_log(log_file)
    #not doing this one print(urls_with_counts, 'url')
    # sort them by total requests descending
    #not doing this onesorted_by_count = sorted(urls_with_counts.items(), key=itemgetter(1), reverse=True)
    # this on eeither print(sorted_by_count)
    ####print(find('\x04\x01\x00P\xC6\xCE\x0Eu0\x00',''))
