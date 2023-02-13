#Program1
#(WAP) to compute x*n of given two integers x and n.
# x = int(input("enter a number"))
# n = int(input("enter power"))
# z = (x**n)
# print(z)


#Program2
#(WAP) for calculating simple interest
# print  ("SIMPLE INTEREST CALCULATION\n")
# print  ("Enter the following details.")
# p = int(input ("Amount: "))
# n = int(input ("No. of years: "))
# r = int(input ("Rate of Interest: "))
# i = (p*n*r) / 100
# print  ("\n the interest is : " + str(i))


#Program3
#(WAP) to accept a no. from the user and display whether it is an even no. or odd no.
# x = int(input("enter no:"))
# if (x%2==0):
#     print("even no.")
# else:
#     print("odd no")


#Program4
#(WAP) to accept percentage of a student and display its grade accordingly.
# perc = float(input("enter percentage of a student : "))  #statment1
# if perc > 85:                                            #condition1
#     print('A')
# elif perc >70 and perc <=85:                             #condition2
#     print('B')
# elif perc >60 and perc <=70:                             #condition3
#     print('C')
# elif perc >45 and perc <=60:                             #condition4
#     print('D')
# else:
#     print('E')



#Program5
#(WAP) to print fibonacci series up to ceratin limit.
# i = int(input("enter the limit"))
# x = 0
# y = 1
# z = 1
# print("Fibonacci series\n")
# print(x,y,end="")
# while(z<=i):
#     print( z, end=' ')
#     x=y
#     y=z
#     z=x+y


#Program6
#(WAP) to display prime no. up yo a certain limit.
# x = int(input("enter limit"))
# for num in range (x+1):
#     i = 2
#     while i<num%i ==0:
#         break
#     i = i+1
# else:
#     print(num,'is a prime no')


#Program7
#(WAP) to accept a number, find and display whether it's a Armstrong no. or not
# num = int(input("enter 3 digit number"))
# f = num
# sum = 0
# while(f>0):
#     a = f%10
#     f = int(f/10)
#     sum = sum+(a**3)
# if (sum==num) :
#     print("it is a Armstrong no",num)
# else:
#     print("it is not a Armstrong no",num)


#Program8
#(WAP) to accept a no. and find out whether it is a perfect no. are not
# i = 1
# s = 0
# num = int(input("enter no"))
# while i<num:
#     if num%i == 0:
#         s +=1
#     i = i+1
# if s==num:
#     print("it is a perfect no")
# else:
#     print("it is not perfect no")


#Program9
#(WAP) to print the sum of the series 1+x1/1!+x2/2!+......xn/(n)!- exponential series.
# x = float(input('enter value of x:'))
# y = int(input('enter limit'))
# s = 0
# for i in range(0,s+1):
#     fact=1
#     for k in range(1,i+1):
#        fact=fact*k
#     s+=(-x**i)/fact(i)
# print(s)


#Program10
#(WAP) tp print the following pattern:
# 1
# 12
# 123
# i = 1
# while i<=3:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j = j+1
#     print ()
#     i = i+1


#Program11
#(WAP) to accept a string and display whether it is a palindrome.
# str = input("enter the string")
# l = len(str)
# p = 1-1
# index = 0
# while (index<p):
#     if(str[index]==str[p]):
#         index=index+1
#         p=p-1
#     else:
#         print("string is not a palindrome")
#         break
# else:
#     print("string is a palindrome")


#Program12
#(WAP) that counts the number of alphabets and digits, uppercase letters, lowercase letter, spaces and other characters in the string entered.
# strl = input('enter a string')
# n=c=d=s=u=l=o=0
# for ch in strl:
#     if ch.isalnum():
#         n+=1
#        if ch.isupper():
#             u=u+1
#         elif ch.islower():
#             l=1+1
#         elif ch.isalpha():
#             c=c+1
#     if ch.isdigit():
#         d=d+1
#     elif ch.isspace():
#         s=s+1
#     else:
#         o=o+1
# print('no of alphabets and digits',n)
# print('no of capital alphabets',u)
# print('no of small alphabets',1)
# print('no of digits',d)
# print('no of spaces',s)
# print('no of other characters',o)    


#Program13
# (WAP) to accept a string (a sentence) and returns a string having first letter of each word in capital letter.
# strl = input("enter a string:")

# print("original strng",strl)
# str2 = ""
# x = strl.split()
# for a in x:
#     str2 += a.capitalize()+" "
#     print(str2)


#Program14
#(WAP) to remove all odd numbers from the given list.
# def main():
#     L=[2,7,12,5,10,15,23]
#     for i in L:
#         if i%2==0:
#             L.remove(i)
#     print(L)    
# main()


#Program15
#(WAP) to display second largest element of a given list.
# L = [41,6,9,13,4,23]
# m = max(L)
# secmax = L[0]
# for i in range (1,len(L)):
#     if L[i]>secmax and L[i]<m:
#         secmax = L[i]
# print(secmax)














