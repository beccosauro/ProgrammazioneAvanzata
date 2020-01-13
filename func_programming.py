### EXCERCISE 1 ###
import itertools,fractions,functools,math
print(sum([x for x in range(1000) if x%3==0 or x%5==0]))

def lcm(a,b):
    return a/fractions.gcd(a,b)*b      

print(functools.reduce(lcm,range(1,20)))
print(functools.reduce(lambda x,y: int(x)+int(y), str(2**1000)))

def fibo():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

f = enumerate(fibo())
x = 0
while len(str(x)) < 1000:
    i,x = next(f)

print("The %d-th term has %d digits"%(i+1,len(str(x))))
