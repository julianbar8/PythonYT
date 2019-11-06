def add(x,y):
    """add function"""
    return x+y

def sub(x,y):
    """subtract function"""
    return x-y

def multiply(x,y):
    """division function"""
    return x * y
def divide(x,y):
    """multiplication function"""
    if y == 0:
        raise ValueError('Cant divide by 0')
    return x / y

print(add(10,5))
