def check(x):
    print(check(x))

m = int(input("Enter a No : "))
s = ((lambda v : v%2 ==0)(m))
if(s == True):
    print("Even No")
elif(s == False):
    print("Odd No")
