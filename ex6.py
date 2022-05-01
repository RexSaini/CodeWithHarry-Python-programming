#Exercise6
import random
print("Welcome to SNAKE-WATE-GUN")
a=True
lst=["Snake", "Water", "Gun"]
i=0
n=int(input("Enter number of rounds you want to play: "))
while a:
    computer_points=0
    player_points=0
    while i<n:
        print("Round-",(i+1))
        computer_choice=random.choice(lst)
        player_choice=input(f"Press 'S' for {lst[0]}, 'W' for {lst[1]}, 'G' for {lst[2]}: ")
        if player_choice=="S" or player_choice=='s':
            if computer_choice==lst[1]:
                player_points+=1
            elif computer_choice==lst[2]:
                computer_points+=1
    
        elif player_choice=="W" or player_choice=="w":
            if computer_choice==lst[0]:
                computer_points+=1
            elif computer_choice==lst[2]:
                player_points+=1

        elif player_choice=="G"or player_choice=="g":
            if computer_choice==lst[0]:
                player_points+=1
            elif computer_choice==lst[1]:
                computer_points+=1
        else:
            print("Error! Please press correctly")  #This round will be played again
            i-=1
        i+=1
    
    print()
    print("Result: ")
    print("You:",player_points,"\t","Computer:",computer_points)
    if player_points==computer_points:
        print("TIE")
    elif player_points>computer_points:
        print("YOU WIN")
    else:
        print("YOU LOSE")
        
    print()
    b=input("Press y for continue, any other key for exit: ")
    if b=="y" or b=="Y":
        a=True
    else:
        a=False
    i=0
print()
print("END")
print("Thank you for playing")