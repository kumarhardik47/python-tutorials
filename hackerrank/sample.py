import os


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    l = sorted(arr)
    length = len(l)
    for i in range(length):
	print l[length-(i+2)], l[length-(i+1)]
        if l[length-(i+2)] == l[length-(i+1)]:
            continue
        else:
            print l[length-(i+2)]
	    break
