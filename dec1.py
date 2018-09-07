from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
	print args,kwargs
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))
#print(print_number(222,{'a':2}))




for num in range(1, 6):
    print(print_number(num))


#print dir(sleep_decorator)
