from enum import Enum
import inspect

class NumbersEnum(Enum):
    """
        Catalog of numbers
    """
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

def alias(*aliases):
    def decorator(func):
        def wrapper(*args, **kwargs):
            caller_name = inspect.currentframe().f_back.f_code.co_name

            result = func(*args, alias=caller_name, **kwargs)
            
            return result
        
        return wrapper
    return decorator

def plus(number):
    def wrapper(y):
        result = number + y
        print(result)

    return wrapper
    
def minus(number):
    def wrapper(y):
        result = y - number
        print(result)

    return wrapper
    
def times(number):
    def wrapper(y):
        result = number * y
        print(result)

    return wrapper
    
def divided_by(number):
    def wrapper(y):
        result = y // number
        print(result)

    return wrapper

@alias("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
def my_function(param, *args, **kwargs):
    my_number = NumbersEnum[kwargs.get('alias')].value
    if param == 'default':
        return my_number  
    else:
        result = param(my_number)
        return result    

def zero(param='default'):
    return my_function(param)
def one(param='default'):
    return my_function(param)
def two(param='default'):
    return my_function(param)
def three(param='default'):
    return my_function(param)
def four(param='default'):
    return my_function(param)
def five(param='default'):
    return my_function(param)
def six(param='default'):
    return my_function(param)
def seven(param='default'):
    return my_function(param)
def eight(param='default'):
    return my_function(param)
def nine(param='default'):
    return my_function(param)


if __name__ == '__main__':
    four(times(five()))
    one(plus(eight()))
    seven(minus(three()))
    nine(divided_by(three()))
    