'''
l = []
l = [[37.2, 'Tina'], [37.21, 'Berry'], [37.21, 'Harry'], [39, 'Harsh'], [41, 'Akriti']] 
for i in range(len(l)):
    print len(l)
    s = l[i+1]
    t = l[i+2]
    #print "s,t", s,t,
    if s[0] == t[0]:
        print s[1]
        print t[1]
        break
    else:
        print s[1]
        break
'''
l = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([score,name])
    
for i in range(len(l)):
    s = l[i+1]
    t = l[i+2]
    print "s,t", s,t
    if s[0] == t[0]:
        print s[1]
        print t[1]
        break
    else:
        print s[1]
        break

