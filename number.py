number1 = int(input("1. ").strip())
number2 = int(input("2. ").strip())
number3 = int(input("3. ").strip())

if number1 > number2 and number1 > number3:
    print("The biggest number is:",number1,">_<")
elif number2 > number1 and number2 > number3:
    print("The biggest number is:",number2,">_<")
elif number3 > number1 and number3 > number2:
    print("The biggest number is:",number3,">_<")
else:
    print("Please enter a different number T_T")