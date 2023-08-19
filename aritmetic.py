def zero(param='default'):
    if param == 'default':
        return 0
    else:
        result = param(0)
        return result    
    
def one(param='default'):
    if param == 'default':
        return 1
    else:
        result = param(1)
        return result    
    
def two(param='default'):
    if param == 'default':
        return 2
    else:
        result = param(2)
        return result    
        
def three(param='default'):
    if param == 'default':
        return 3
    else:
        result = param(3)
        return result    
    
def four(param='default'):
    if param == 'default':
        return 4
    else:
        result = param(4)
        return result    

def five(param='default'):
    if param == 'default':
        return 5
    else:
        result = param(5)
        return result    
    
def six(param='default'):  
    if param == 'default':
        return 6
    else:
        result = param(6)
        return result    

def seven(param='default'):
    if param == 'default':
        return 7
    else:
        result = param(7)
        return result    
    
def eight(param='default'):
    if param == 'default':
        return 8
    else:
        result = param(8)
        return result    
        
def nine(param='default'):
    if param == 'default':
        return 9
    else:
        result = param(9)
        return result    
        
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
    