a = int(input("Enter No : "))
list= [ ]
t=99999999999
for i in range(0,a):
    c = int(input())
    list.append(c)
    if(c<t):
        c1=t;
        t=c;

print(c1);