# Find Factorial of  Each List  No and Update them.

def fact(x):
    k=1
    for i in range(1,x+1):
        k=k*i
    return k
nums=[5,6,7,8,9]
s=list(map(fact,nums))
print(s)