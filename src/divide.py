

def divide(x, y):
    """ computes x/y and returns quotient and remainder
    Args:
        x: int 
        y: int
    Returns:
        (quotient, remainder)
    """
    r = x
    q = 0

    while r>=y:
        q += 1
        r -= y 

    return (q,r)




# x/2^ky
def divide2(x, y): 
    q = 0
    power = 32
    yp = y << power
    while (x >= y):
        while (yp > x ):
            power-=1
            yp = y << power 
        q += 1<<power
        x -= yp
        print (yp, x, q)
    return (q,x)


res = divide(11,2)
print(res)

res = divide2(11,2)
print(res)
