"""TODO 1)	Implement a function decorator that reverses the target positional arguments
 (however has no effect on keyword arguments)"""


def reverse_func_decorator(func):
    def wrapper(*args, **kwargs):
        args = (arg * -1 for arg in args)
        try:
            output = func(*args,**kwargs)
        except TypeError:
            print("Please check your input type")
        return output
    return wrapper


@reverse_func_decorator
def sub(a, b):
    return a-b


print(sub(3, 2) == -1)   #Note this calculated b-a
print(sub(a=3, b=2) == 1)   #Note this calculated a-b
