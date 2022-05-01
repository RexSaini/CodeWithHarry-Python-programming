"""Exercise2
Faulty Calculator"""
print("'+' for addition, '-' for substraction, '*' for multiplication, '/' for division")
num1=eval(input("Enter first number: "))
op=input("Enter operator: ")
num2=eval(input("Enter second number: "))
if num1==45 and num2==3 and op=='*':
    print("Answer: 555")
elif num1==56 and num2==9 and op=='+':
    print("Answer: 77")
elif num1==56 and num2==6 and op=='/':
    print("Answer: 4")
elif op=='+':
    print("Answer:", (num1+num2))
elif op=='-':
    print("Answer:", (num1-num2))
elif op=='*':
    print("Answer:", (num1*num2))
elif op=='/':
    print("Answer:", (num1/num2))
else:
    print("Error!")
print("END")