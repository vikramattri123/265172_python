r = input("Enter Text : ")
file2 = open("file1.txt","w")
files = file2.write(r)
if files > 0:
    print("Data Stored")
else:
    print("File is Empty!")
file2.close()