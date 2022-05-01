#Exercise4
while True:
    n=int(input("Enter number of rows: "))
    if n<=0:
        print("Invalid Input")
        break
    _boolean=int(input("Press 1 or 0: "))
    if bool(_boolean)==True:
        for i in range(0,n):
            print((i+1)*"*")
    else:
        for i in range(0,n):
            print((n-i)*"*")
    a=input("Press n or y: ")
    if a=='y' or a=='Y':
        print("Welcome again")
    else:
        print("END")
        break