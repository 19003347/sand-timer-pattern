import math as m
n=int(input('enter a number: '))
m=m.ceil(n/2)
print(m)
dot=0
x=n
for i in range(n,0,-1):
    if i>=m:
        for j in range(dot):
            print('.',end='')
        for j in range(x):
            print('*',end='')
        dot=dot+1
        x=x-2
        print()
        
    elif i<m:
        dot=dot-2
        x=x+4
        for j in range(dot):
            print('.',end='')
        for j in range(x):
            print('*',end='')
        dot+=1
        x-=2
        print()

            
            
    