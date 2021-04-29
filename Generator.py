def prime():
    x=int(input())
    f=0
    v=x
    v=int(v)
    for i in range(2,v):
        if x%i==0:
            f=f+1
    if f==0:
        t="Prime"
        yield t
    else:
        t="Not Prime"
        print(t)
for o in prime():
    print(o)