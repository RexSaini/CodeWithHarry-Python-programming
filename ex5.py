#Exercise5
u="Harry"
v="Rohan"
w="Hamad"

def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    A=True
    a=int(input("Press 1 for Harry, 2 for Rohan, 3 for Hamad: "))
    while A:
        if a==1:
            print()
            print(u)
            b=int(input("Press 1 for food, 2 for exercise: "))
            if b==1:
                with open("Harry_food.txt", "a") as f:
                    c=input("Enter food: ")
                    f.write(str(getdate())+"\t"+c+"\n")
            elif b==2:
                with open("Harry_exercise.txt", "a") as f:
                    d=input("Enter exercise: ")
                    f.write(str(getdate())+"\t"+d+"\n")
            else:
                print("Error!")
                continue
                
            _a=input(("To continue press 'Y', to exit press any other key: "))
            if _a=="y" or _a=="Y":
                A=True
            else:
                A=False
            
        elif a==2:
            print()
            print(v)
            _b=int(input("Press 1 for food, 2 for exercise: "))
            if _b==1:
                with open("Rohan_food.txt", "a") as f:
                    _c=input("Enter food: ")
                    f.write(str(getdate())+"\t"+_c+"\n")
            elif _b==2:
                with open("Rohan_exercise.txt", "a") as f:
                    _d=input("Enter exercise: ")
                    f.write(str(getdate())+"\t"+_d+"\n")
            
            else:
                print("Error!")
                continue
                
            _a=input(("To continue press 'Y', to exit press any other key: "))
            if _a=="y" or _a=="Y":
                A=True
            else:
                A=False
        
        elif a==3:
            print()
            print(w)
            __b=int(input("Press 1 for food, 2 for exercise: "))
            if __b==1:
                with open("Hamad_food.txt", "a") as f:
                    __c=input("Enter food: ")
                    f.write(str(getdate())+"\t"+__c+"\n")
            elif __b==2:
                with open("Hamad_exercise.txt", "a") as f:
                    __d=input("Enter exercise: ")
                    f.write(str(getdate())+"\t"+__d+"\n")
            else:
                print("Error!")
                continue
            
            _a=input(("To continue press 'Y', to exit press any other key: "))
            if _a=="y" or _a=="Y":
                A=True
            else:
                A=False
                
        else:
            print("Error!")
            break

def retrieve():
    p=int(input("Press 1 for Harry, 2 for Rohan, 3 for Hamad: "))
    if p==1:
        print()
        print(u)
        q=int(input("Press 1 for food, 2 for exercise: "))
        if q==1:
            with open("Harry_food.txt") as f:
                r=f.read()
                print(r)
        elif q==2:
            with open("Harry_exercise.txt") as f:
                s=f.read()
                print(s)
        else:
            print("Error!")
        
    elif p==2:
        print()
        print(v)
        _q=int(input("Press 1 for food, 2 for exercise: "))
        if _q==1:
            with open("Rohan_food.txt") as f:
                _r=f.read()
                print(_r)
        elif _q==2:
            with open("Rohan_exercise.txt") as f:
                _s=f.read()
                print(_s)
        else:
            print("Error!")
                
    elif p==3:
        print()
        print(w)
        __q=int(input("Press 1 for food, 2 for exercise: "))
        if __q==1:
            print()
            print()
            with open("Hamad_food.txt") as f:
                __r=f.read()
                print(__r)
        elif __q==2:
            with open("Hamad_exercise.txt") as f:
                __s=f.read()
                print(__s)
        else:
            print("Error!")

print("Welcome to Health Management System")
x=int(input("Press 1 for log, 2 for retrieve: "))
if x==1:
    log()
elif x==2:
    retrieve()
else:
    print("Error!")