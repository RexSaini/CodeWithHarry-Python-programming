#Fibonacci Sequence
def func(n):
   if n <= 1:
       return n
   else:
       return(func(n-1) + func(n-2))

n=int(input("Enter number of terms: "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(func(i),end=" ")