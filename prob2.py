# Practice problem2
try:
    apples = int(input("Enter the number of apples: "))
    mn = int(input("Enter the minimum number to check: "))
    mx = int(input("Enter the maximum number to check: "))
except ValueError:
    print("Intergers value only!")
    exit()

if (mn==mx):
    print("Not a range")

for i in range(mn, mx+1):
    if apples%i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")