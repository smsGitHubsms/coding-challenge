file = open("demo.txt","w")
file.write("Hello How are you ??")
file.close()

file=open("demo.txt","r")
contents = file.read()
print("The content in the file is: ",contents)
file.close()

file=open("demo.txt","a")
file.write("\nHope all going fine")
file.close()


