a = int(input("enter your number: "))
#นับเศษ ถ้าถึง 2 จะหยุด
nub = 0

for i in range(1,a+1,1):
    if a % i == 0:
        nub = nub + 1

if nub == 2:
    print("prime number")
else:
    print("not prime")


