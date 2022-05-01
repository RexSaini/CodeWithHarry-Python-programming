# Practice problem4
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    n = int(input("Enter the number of test cases: "))
    numbers = []
    print()
    for i in range(n):
        number = int(input("Enter the number:"))
        numbers.append(number)
    print()
    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
