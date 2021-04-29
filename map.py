# Using Map we can find the prime no , Non-Prime Number is represented as None
def prime(x):
    flag=0
    m=[]
    for i in range(2,x):
        if x%i == 0:
            flag=flag+1
        if x==2:
            flag=0
    if flag == 0:
        return x

nums = [3,5,8,11]
s=list(map(prime,nums))
print(s)