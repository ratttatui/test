age = int(input("Enter your age: "))
license = input("Do you have a Driving license?(Yes/No): ").lower().strip()

if age >= 18 and license == "yes":
    print("You can drive! :D")
else:
    print("You can't drive :(")