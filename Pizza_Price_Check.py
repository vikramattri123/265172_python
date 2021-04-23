a = int(input("Enter Slices you want  : "))
t=0
if a%2==0:
    t=a*120.00
elif a%2 ==1:
    t=a*123.0

print("You bill amount is : ",t)
