def prime(x):
    flag=0
    for i in range(1,x):
        if x%i == 0:
            flag=flag+1
    if flag == 0:
        return x

nums = [3,5,8,11]
s=list(filter(prime,nums))
print(s)