# รับเลข 3 ตัว หาว่าตัวไหนมากที่สุด (ใช้ and เทียบทีละคู่)

print("Enter 3 numbers:")
number1 = int(input("1. "))
number2 = int(input("2. "))
number3 = int(input("3. "))

if number1 == number2 or number1 == number3 or number2 == number3:
    print("Please enter different numbers T_T")
elif number1 > number2 and number1 > number3:
    print("The biggest number is:",number1,">_<")
elif number2 > number1 and number2 > number3:
    print("The biggest number is:",number2,">_<")
elif number3 > number1 and number3 > number2:
    print("The biggest number is:",number3,">_<")
