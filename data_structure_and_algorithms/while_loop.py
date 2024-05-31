def number(num):
    for i in range(1,num+1):
        print(i)
if __name__ == "__main__":
     num=int(input(" enter number"))
     number(num)


for x in range(1,5+1):
    if (x%2==0):
        print(x**2)

name=input("enter name\n")
while name=="":
    print(" you did not enter name")
    name = input("enter name\n")
print(f" hello {name} welcome")



while True:
    name=input(" enter nane2\n")
    if name=="afidhu":
        print(f" welcom ",name)
        break
print(" good morning")

while True:
    age= int(input(" enter age"))
    if age>18:
        print(" you are  allowed")
        break
print(f" age {age} you are not child")



while True:
    numbers = int(input(" enter posive number\n"))
    if (numbers>0):
        print(f"number is {numbers} is  positive")
        break



food=input(" enter food\n")
while not food=="q":
    print(f" the food {food} not\n")
    food = input(" enter food")
print(" good")

num=int(input(" enter number  btn 1 to 10\n"))
while num<1 or num>10:
    print(f" the number {num}is not allow ")
    num = int(input(" enter number  btn 1 to 10\n"))
print(f" the number {num} is tbn  ")

n=int(input(" enter row "))
for x in range(0,n+1):
    for y in range(0,x+1):
        print("*", end="")
    print()



