#form all subsets from a list that sums to 4.

def ssum(lst,sum):
    current = ""
    ssum_h(lst, len(lst), current, sum)

def ssum_h(lst, n, subset, sum):
	if sum == 0:
	    print subset
	    return
	if n == 0:
	    return
	if lst[n-1] <= sum:
	    ssum_h(lst, n-1, subset, sum)
	    ssum_h(lst, n-1, subset+`lst[n-1]`+" ", sum-lst[n-1])
	    print '*' * 80
	    print  "#",subset, subset+`lst[n-1]`, sum-lst[n-1], "#"
	    print '-' * 80
	else:
	    ssum_h(lst, n-1, subset, sum)

if __name__ == "__main__":
    #enter space separated numbers
    lst = [int(x) for x in raw_input().split()]
    #enter a targt number
    sum = int(input())
    #print lst,sum
 
    ssum(lst,sum)


	
    
