def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
num = 4
print("Factorial of",num,"is",fact(num))



def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)
num=int(input("enter the number"))
print("factorial of", num, "is", fact(num))

