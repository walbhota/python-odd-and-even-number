num = int(input("Enter the number: "))
if num <= 99 and num % 2 == 0:
    print("This is an Even number")
elif num <= 99 and num % 2 != 0:
    print("This is an Odd number")
else:
    print("This number is not included")
