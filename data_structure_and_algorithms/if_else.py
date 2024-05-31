

element = int(input(" enter size of list \n"))
numbers=[]
sum=0
k=[]
for y in range(element):
    x = int(input(" enter number"))
    k.append(x)
    if (x%2)==0:
        sum=sum+x
        numbers.append(sum)
print(" the list is ", k)
print(" sum of even number in list ",k," is ", numbers)

print("\n")

element = int(input(" enter size of list \n"))
numbers=[]
for y in range(element):
    x = int(input(" enter number"))
    numbers.append(x)
print(numbers)



name="afidhu"
acl="xyz"
marks=56
if acl=="xyz":
    if name=="afidhu":
        print("welcome xyz college ", marks)

y=9
t=3
x=2
if x>y and x>t:
    print( " x is greater ")
else:
    if y>t:
        print(" y nis greater")
    else:
        print("t is greater")
n=9
for x in range(1,11):
    table= n * x
    print(n, "*",x,"=",table)

print("\n")

list_1=[2,4,6]
list_2=[2,4,6]
for y in list_1:
    for x in list_2:
        if y==x:
            continue
        print(y, "*", x, " =", x*y)

# prime number
lower= int(input(" enter lower number \n"))
upper= int(input(" enter upper number \n"))
for number in range(lower,upper+1):
    if number>1:
        for x in range(2,number):
            if (number%x)==0:
                break
        else:
            print(number)