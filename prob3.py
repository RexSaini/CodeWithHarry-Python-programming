# Practice problem3
print("Enter the numbers of the list one by one")
size = int(input("Enter size of list: "))

mylist = []

for i in range(size):
    mylist.append(int(input("Enter list element: ")))
    
print(f"Your list is {mylist}")

print()

print("Method1!")
reverse1 = mylist[:]
reverse1.reverse()
print(f"Your list {mylist} \nReversed list is {reverse1}")

print("Method2!")
reverse2 = mylist[::-1]
print(f"Your list {mylist} \nReversed list is {reverse2}")

print("Method3!")
reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i] 

print(f"Your list {mylist} \nReversed list is {reverse3}")

print()

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")