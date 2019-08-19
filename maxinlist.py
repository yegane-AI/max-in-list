#find max
x = int(input("How many numbers would you type: "))
list=[]
for i in range(1,x+1):
    y = int(input("Type a number: "))
    list.append(y)
print("maximum is: ",max(list))

input("Press Enter to exit! ")
