from random import*
def isPrimeNumber(n):
    cnt=0
    d=n-1
    while d%2==0:
        cnt+=1
        d//=2
    k=0
    while k<100:
        k+=1
        a=randint(2,n-2)
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        i=1
        while i<cnt:
            i+=1
            x=x*x%n
            if x==n-1:
                break
        if x==n-1:
            continue
        return 0
    return 1    
def getPrimeNumber(t):
    a=getrandbits(t)
    while isPrimeNumber(a)==0:
        a=getrandbits(t)
    else:
        return a
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)
def ex_gcd(a,b):
    if b==0:
        return 1,0;
    x,y=ex_gcd(b,a%b)
    return y,x-a//b*y    
def RSA():
    p=getPrimeNumber(800)
    q=getPrimeNumber(800)
    n=p*q
    fi=(p-1)*(q-1)
    e=randint(2,n)
    while gcd(e,fi)!=1:
        e=randint(2,n)
    d,k=ex_gcd(e,fi);
    print(e)
    print(d)
    print(n)
    print(e*d%fi)
    return e,d,n
e,d,n=RSA()