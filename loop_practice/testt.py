# a =int(input("input: "))
# print("*"*a)

# a =(input("name: "))
# print(f"hello, {a}")

# a = (input("name: "))
# print(f"hello, {a} your name legnth is {len(a)}")

# a = (input("name: "))
# if a == "mel":
#     print(f"hello, mr.{a}")
# else:
#     print(f"hello, ms.{a}")

# for i in range(1,11):
#     print(i)

# for i in range(1,13):
#     print(f"2*{i} =",2*i," ".ljust(4), f"3*{i} =",3*i," ".ljust(4))

for i in range(1,13):
    for j in range(2,20):
        print(f"{j}*{i:<2} = {j*i:<3}", end=" ")
        if j == 19:
            print()