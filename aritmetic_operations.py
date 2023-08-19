from enum import Enum

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

def caller_operation(param, number):
    result = param(number)
    return result    

def zero(param='default'):
    my_number = NumbersEnum.zero.value
    return my_number if param == 'default' else caller_operation(param, my_number)
    
def one(param='default'):
    my_number = NumbersEnum.one.value
    return my_number if param == 'default' else caller_operation(param, my_number)
    
def two(param='default'):
    my_number = NumbersEnum.two.value
    return my_number if param == 'default' else caller_operation(param, my_number)
        
def three(param='default'):
    my_number = NumbersEnum.three.value
    return my_number if param == 'default' else caller_operation(param, my_number)
    
def four(param='default'):
    my_number = NumbersEnum.four.value
    return my_number if param == 'default' else caller_operation(param, my_number)

def five(param='default'):
    my_number = NumbersEnum.five.value
    return my_number if param == 'default' else caller_operation(param, my_number)
    
def six(param='default'):  
    my_number = NumbersEnum.six.value
    return my_number if param == 'default' else caller_operation(param, my_number)

def seven(param='default'):
    my_number = NumbersEnum.seven.value
    return my_number if param == 'default' else caller_operation(param, my_number)
    
def eight(param='default'):
    my_number = NumbersEnum.eight.value
    return my_number if param == 'default' else caller_operation(param, my_number)
        
def nine(param='default'):
    my_number = NumbersEnum.nine.value
    return my_number if param == 'default' else caller_operation(param, my_number)
        
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

if __name__ == '__main__':
    four(times(five()))
    one(plus(eight()))
    seven(minus(three()))
    nine(divided_by(three()))
    