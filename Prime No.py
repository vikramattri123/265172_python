Num = int(input("Enter a Number : "))

if(Num == 1):
    {
        print("Not Prime")
    }
else:
  flag = 0
  for i in range(2,Num):
       if Num%2 == 0:
          flag=1

  if(flag==0):
      {
          print("Prime No")
      }

  else:
      {
          print("Not Prime")
      }

