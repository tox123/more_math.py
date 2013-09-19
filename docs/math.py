from cmath import *
from random import *
from sys import *
from os import *
from math import *

def cbrt(number, min_of_test_range, max_of_range):   #guesses and checks for a cube root
    n_1 = number
    __min__ = min_of_test_range
    m_a_x = max_of_range
    m_m_l = 0
    for x in range (__min__,m_a_x):
        #this does the guess 'n check part
        if x**3 == n_1:
            return x
        else:
            m_m_l = m_m_l + 1

    if m_m_l == (m_a_x-__min__):
        return 'the number\'s cube root is not in the range you have given me or it could be irrational'

def selfexpont(number):   #this : exponts :: multiplication : addition
    n_2 = number
    return (n_2**n_2)

def add (number1 , number2):  #it adds numbers what else would it do?!?
    return (number1+number2)

def add_ (number1 , number2):  #hahaha it 'adds' numbers
    return float((str(number1) + str(number2)))


def cbrtmulti(number_min , number_max , minrange , maxrange):
    max_ = maxrange
    min_ = minrange
    med = (min_+max_)/2
    if med * 2 % 2 != 0:
        med = med + 1
    else:
        pass
    for x in range (number_min , number_max):
        #here it does the multiple cube roots
        for y in range (min_ , (med-1)):
            for z in range (med , max_):
                print (cbrt(x , y , z))

def sqrtmulti(number_min , number_max , minrange , maxrange):
    max_ = maxrange
    min_ = minrange
    med = (min_+max_)/2
    for x in range (number_min , number_max):
        #here it does the multiple square roots
        for y in range (min_ , (med-1)):
            for z in range (med , max_):
                print (sqrt(x))

def substrnum(string , number):
    len_ = len(string)-1
    newstring = ''
    for x in range (0, len_):
        newstring = newstring + string[x]
        if x == len_ - number:
            return (newstring)
        else:
            pass

def divstr(string , number):
    len_ = len(string)+1
    f=0
    for x in range (0,len_):
        if x % number == 0:
            print (string[f:x])
            f = x

def prime(number):
    if number == 1 or number == 0:
        raise ValueError("1 and 0 are neither prime nor composite")
    for x in range (2,number-1):
        if number % x == 0:
            return False
        else:
            pass
    return True

def composite(number):
    return not prime(number)

def anyrt(exponint,base):
    e=exponint
    b=base
    n=b**(1/e)
    return n

def anymulti(exponint , number_min , number_max):
    for x in range (number_min , number_max):
        #here it does the multiple roots
        print (anyrt(exponint,x))

def eRr0r (type_, txt):
    typ = lower(type_)
    if txt == None:
        raise RuntimeError('must have some text!!!')
    if typ == 'value':
        raise ValueError(txt)
    elif typ == 'overflow' or typ == 'over':
        raise OverflowError(txt)
    elif typ == 'run' or typ == 'time' or typ == 'runtime':
        raise RuntimeError(txt)
    else:
        raise RuntimeError(txt + 'is not a error or it is not in my database or it is not a error')

def prime_generator():
    from random import randint
    prime_ = randint(6,10000)*6
    if prime_ % 2 == 0:
        prime_ = prime_+1
    else:
        prime_ = prime_-1
    if prime(prime_) == True:
        return prime_
    else:
        prime_ = randint(6,10000)*6
        if prime_ % 2 == 0:
            prime_ = prime_+1
        else:
            prime_ = prime_-1
        if prime(prime_):
            return prime_
        else:
            prime_ = randint(6,10000)*6
            if prime_ % 2 == 0:
                prime_ = prime_+1
            else:
                prime_ = prime_-1
            if prime(prime_):
                return prime_
            else:
                raise RuntimeError('try again')

def prime(number):
    if number == 1 or number == 0:
        return False
    for x in range (2,number-1):
        if number % x == 0:
            return False
        else:
            pass
    return True

def prime_generator(least):
    from random import randint
    prime_ = randint(least,((100*least+5)%19)+least)*6
    if prime_ % 2 == 0:
        prime_ = prime_+1
    else:
        prime_ = prime_-1
    if prime(prime_) == True:
        return prime_
    else:
        prime_ = randint(6,10000)*6
        if prime_ % 2 == 0:
            prime_ = prime_+1
        else:
            prime_ = prime_-1
        if prime(prime_):
            return prime_
        else:
            prime_ = randint(6,10000)*6
            if prime_ % 2 == 0:
                prime_ = prime_+1
            else:
                prime_ = prime_-1
            if prime(prime_):
                return prime_
            else:
                prime_generator(least+1)

def prime_to(n):
    x = []
    for y in range(n):
        if prime(y):
            x.append(x)
        else:
            continue
    return x

def count(start,stop,step):
    for x in range(start, stop):
        yield (x)

def substrstr(str1 , str2):
    new = ''
    li = []
    il = []
    for x in str1:
        li.append(x)
    for x in str2:
        il.append(x)
    for x in li:
        for y in il:
            if y != x:
                new += y
                break
            else:
                continue
    return new

def area_of_sphere(radius):
    4*pi*radius**2

def premution (a,b):
    w = 0
    x = 1
    while w < b:
        x *= a-w
        w += 1
    return w

p = premution

def combination(x,y):
    ansewr = p(x,y)/p(y,y)
    return ansewr

c = combination

def fact(n):
    r = 1
    while n > 0:
        r *= n
        n -= 1
    return r

def info():
    return ('made by Scott Whalen Blair on 7/10/2013 with Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] more math v1.2')
