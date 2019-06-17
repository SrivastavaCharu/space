n=raw_input('Enter a number')
n=int(n)
m=n

c=(n-1)*2
sp=0
for x in range(n,0,-1):
    for x in range(1,n+1):
        print x,
    if(sp<=c):
        for x in range(0,sp):
            print(' '), 
               
    for x in range(n,0,-1):
        print x,
    
                    
    print
    n-=1
    sp+=2

s=0
c=(m-1)*2
for i in range(1,m+1):
    for j in range(1,i+1):
        print j,
    for a in range(0,c):
        print(' '),
    for b in range(s+1,0,-1):
            print b,
    s+=1
    c-=2
    print
    
    
    

    



