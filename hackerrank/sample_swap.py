def swap_case(s):
    retval = ""
    for i in s:
        if i.islower():
            retval = retval+i.upper()
	    print "#",retval
        else:
            retval = retval+i.lower()
	    print "-",retval
    return retval

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
