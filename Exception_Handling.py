try:
    a = int(input())
    b=a/0
except:
    print("Error occur !")
finally:
    print("Execute Everytime")
