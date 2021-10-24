print("Welcome to FizzBuzz!")

random_number = int(input("Enter a number between 1 and 100: "))

for x in range(1, random_number+1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
