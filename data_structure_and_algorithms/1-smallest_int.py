
# this is first question

def get_smallest_integer(my_list):
    small=my_list[0]
    for i in list:
        if i<small:
            small=i
    return small

if __name__ == "__main__" :
     list = [10, 9, 7, 10, 6, 5, 7, 24, 6]
     print(get_smallest_integer(list))


""""
list=[10, 9, 7, 10, 6, 5, 7, 24, 6]
print("smallest in ",list,"is")
print(get_smallest_integer(list))"""


# this is second question
def find_first_occurrence(my_list, num):
     count = 0
     for ele in my_list:
         if (ele == num):
             count = count + 1
     return count
if __name__ == "__main__" :
    my_list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    num = 8
    print('{} has occurred {} times'.format(num, find_first_occurrence(my_list, num)), f" at index {num}")

#this is question number 3
def print_right_triangle(height):
    for triangle in range(1,height+1):
        for display in range(triangle):
            print("*", end="")
        print("")
if __name__ == "__main__" :
    print_right_triangle(6)



#this is four question it not complete
"""number = 5
fact = 1
for i in range(1, number + 1):
    if (i%2==0):

        fact = i * i
print("The factorial of 5 is : ")
print(fact)"""
def calculate_prime_factors(N):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors


input_number = 20
output = calculate_prime_factors(input_number)
print("Prime factors of {} are {}".format(input_number, output))
input_number = 1260
output = calculate_prime_factors(input_number)
print("Prime factors of {} are {}".format(input_number, output))

Number = int(input(" Please Enter any Number: "))

for i in range(2, Number + 1):
     if (Number % i == 0):
         isprime = 1
         for j in range(2, (i // 2 + 1)):
             if (i % j == 0):
                 isprime = 0
                 break

         if (isprime == 1):
             print(" %d is a Prime Factor of a Given Number %d" % (i, Number))

# this is qn 4
"""def factorize(number):
    list = []
    for prime in range(1, number+1):
        if (number%prime==0):
            list.append(prime)
    print(list)
user=int(input(" enter number"))
factorize(user)"""
# this 4
def factorize(number):
    cub=[]
    for numbers in range(1,number+1):
        if numbers>1:
            for x in range(2,numbers):
                if (numbers%x)==0:
                    break
            else:

                cub.append(numbers)
    print(f" prime factors of {number} are  \n",format(cub))
if __name__ == "__main__" :
    number=int(input(" enter number to get prime factors \n"))
    factorize(number)

#this is qn 5


#this qn numer 7
def is_prime(number):
    #let given number is "num"
    if number>1:
        for x in range(2,(number//2)+2):
            if (number%x==0):
                return False
                break
        else:
                return True
    else:
        return False

if __name__ == "__main__":
    print(is_prime(11))


#this is number 8
import itertools
def two_indices(nums, target):
    for i, j in itertools.combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]
nums = [2, 6, 7, 15]
target = 9
if __name__ == "__main__":
    result = two_indices(nums, target)
    print(result)


