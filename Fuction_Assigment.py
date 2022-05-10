
# 1. creating table using Function 

n = int(input("Enter the input nnumber"))
def print_table(n): 

    for i in range(1,11): 

        c=n*i
        print(n,' x ', i, ' = ',c) 

print_table(n)


#2(a) sum all the numbers in a list
list1 = [11, 5, 17, 18, 23]

def sumofList(l,s):
   if (s == 0):
    return 0
   else:
     return l[s - 1] + sumofList(l, s - 1)
   
total = sumofList(list1, len(list1))
 
print("Sum of all elements in given list: ",total)

#2(a) sum all the numbers in a Tuple
l1 = [(1, 6), (3, 4), (5, 8)]
print ("The original list is : " + str(l1))
res = [sum(i) for i in zip(*l1)]
print ("The position summation of tuples  : " + str(res))

#3 - Multiplication of  all the numbers in a list
def mul(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(mul([8, 2, 3, 1, 7]))


#3(a)Multiplication of numbers in tupple
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2 ,1,8)
print ("Original Tuple: ")
print(nums)
print("Product of given tuple is :",mutiple_tuple(nums))

#4 -Accepts a string and calculate the number of upper-case letters and lower case  without using function 
str1=str(input("Enter string:"))
c1=0
c2=0
for i in str1:
      if(i.islower()):
            c1+=1
      elif(i.isupper()):
            c2+=1
print("The number of lowercase characters is:")
print(c1)
print("The number of uppercase characters is:")
print(c2)

#4 (a) -Accepts a string and calculate the number of upper-case letters and lower case 
str1=str(input("Enter string:"))
def stringCount(s):
    d={"Upper":0, "Lower":0}
    for c in s:
        if c.isupper():
            d["Upper"]+=1
        elif c.islower():
            d["Lower"]+=1
    else:
        pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["Upper"])
    print ("No. of Lower case Characters : ", d["Lower"])

stringCount(str1)

# 5 - Take a list and return a new list with unique elements of the first list.
ls =[1 ,2 , 3 ,4, 4 ,4 , 5 , 5, 5 ,6]
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print ("given List of Elements is : ",ls)
print("Unique set of Elements ",unique_list(ls)) 

#6 Print given Pascal's triangle
n=int(input("Enter no of rows:"))
print('\n')
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range (1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if (n!=0):
        a[i].append(1)
for i in range(n):
    print("    "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print("{0:6}".format(a[i][j]),end=" ",sep=" ")
    print()

# 7 Function to check whether a string is a palindrome or not

str1=str(input("Enter the input string : "))
def isPalindrome(str1):
    return str1 == str1[::-1]
 
temp =isPalindrome(str1)
if temp:
    print("Yes")
else:
    print("No")


#8 check whether a number is in a given range
n=int(input("Enter the value of n : "))
def T_range(n):
    if n in range(1000,3000):
        print( " Given value  is in the range")
    else :
        print("The number is outside the given range.")
T_range(n)





