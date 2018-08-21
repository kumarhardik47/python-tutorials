from thread import start_new_thread
num_threads = 0
def heron(a):
    """Calculates the square root of a"""
    global num_threads
    num_threads += 1
    print "global", num_threads
    eps = 0.0000001
    old = 1
    new = 1
    print "@@@@@@@@@@@@@@@@@@@@@@@", a
    while True:
        old,new = new, (new + a/new) / 2.0
        print old, new
        if abs(new - old) < eps:
            break
    #num_threads -= 1
    print "#####", num_threads
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))
start_new_thread(heron,(1733,))

c = raw_input("Type something to quit.")
