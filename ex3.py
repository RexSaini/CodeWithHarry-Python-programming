#Exrecise3
num=22
g=9
i=0
while i<=g:
    n=int(input("Enter a number: "))
    print("Guesses left:",(g-i))
    i=i+1
    if n<num:
        print("Increase")
    elif n>num:
        print("Decrease")
    else:
        print("Correct")
        print("You won")
        print("Guesses took:",i)
        break
while i>g:
    print("Game Over")
    break