def outer_func(function):
    def inner_func(*args,**kwargs):
        print("Hacked from functions")
        return function(*args,**kwargs)
    return inner_func # note we are not running it here, it'll return inner_func object, we have to pass parameters when we execute it


class outer_class():
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        print("Hacked from classes")
        return self.func(*args,**kwargs)
@outer_func
def display1(a,b):
    print("I just display {} {}".format(a,b))

@outer_func
def display2(a,b,c):
    print("I just display {} {} {}".format(a,b,c))

display1('a','b')
display2('a','b','c')

@outer_class
def display3(a,b):
    print("I just display {} {}".format(a,b))

@outer_class
def display4(a,b,c):
    print("I just display {} {} {}".format(a,b,c))

display3('a','b')
display4('a','b','c')

