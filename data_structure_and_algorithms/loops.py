s='example'
for x in s:
    print(x, end=" *")

print("\n")
# this is list
my=[3,5,6,7,8,9,0]
sum=0
for x in my:
    sum=sum+x
print(sum)
print(sum/len(my))

#this is tiuple
num=(3,4,5,6,7,8,9,2)
sum=0
for x in num:
    sum=sum+x
    print(sum, " this is tuple")

print(("\n"))
# this is range
for x in range(1,10,2): # this is interval if two no:
    print(x, " this interval of two")

#print table of from user
n=int(input(" enter number \n"))
for x in range(1,11):
    table=n*x
    print(n, " * ",x, " =",table)

print("\n")
list=["ab", "ju", "ge", "re"]
for x in list:
    print(' helloe',x)

print("\n")
name=["kaka","mama", "father"]
for x in name:
    print(" hellow mr & mrs",x)
    for latter in x:
        print(latter)

print("\n")
for i in range(1,10):
    if (i==5):
        break
    print(i)

print("\n")
for i in range(1,10):
    if (i==6):
        continue
    print(i)

print("\n")
num=[2,4,5,6,7,8,9,10]
cube=[]
for i in num:
    cube.append(i**3)
    print(cube)

print("\n")
num=[2,4,5,6,7,8,9,10]
cube=[]
for i in num:
    cube.append(i**3)
print(cube)# look for indentation

print("\n")
#this is pattern print

n=9 #this is number of rows
for i in range(0,n):
    for j in range(0,i +1):
        print("*", end="")
    print()

print("\n")
# THIS IS WHILE LOOP
x=0
while x < 10:
    x=x+1
    print(x, end=" ")

print("\n")

while True:
    name=input(" enter your name \n ")
    if name=="afidhu":
        break
print(" wlcime ", name)

print("\n")
#  lcm 4 and 7
x=0
while True:
    x=x+1
    if not(x%4 or x%7):
        break
print(" the lcm is ",x)

print("\n")
v=1
while v< 5:
    print(v)
    v=v+1
else:
    print(" v is not less than 5")

print("\n")
# average of positive number
sum=0
num=0
count=0
while num>=0:
    num=int(input(" enter positive number\n"))
    if num>=0:
        count=count+1
        sum =sum+num
avg=sum/count
print(" sum is ", sum," for number",count, " the average is ",avg)

print("\n")

list=["3", "7", "9"]
for i in list:
    for x in i:
        print(x, end="%")
    print(" ")

print('\n')
color=['red','blue','pink','yellow','black']
number =['2','3','5','7','9']
for i in color:
    for y in number:
        print(i,y)
    print(' ')

print("\n")
for x in range(11):
    for y in range(x):
        print("*", end="")
    print(" ")
