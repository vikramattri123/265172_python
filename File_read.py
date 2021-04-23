a = open("file1.txt","r+")
read1 = a.read()
if len(read1) > 0:
    print(read1)
else:
    print("File is Empty!")


