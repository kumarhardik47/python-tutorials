import re

count = int(raw_input())
if count > 100:
    exit
for i in range(count):
    name = raw_input()    
    mail = raw_input()
    
    r = re.search(r'[a-zA-Z0-9-.]+@\w+.+[a-z]{3}',mail)
    print r
    if r:
        print name, mail
