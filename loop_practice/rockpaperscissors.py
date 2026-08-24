# a = input("player1: rock, paper or scissors? = ").lower().strip()
# b = input("player2: rock, paper or scissors? = ").lower().strip()

# if (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper") or (a == "paper" and b == "rock"):
#     print("player1 win")
# elif (b == "rock" and a == "scissors") or (b == "scissors" and a == "paper") or (b == "paper" and a == "rock"):
#     print("player2 win")
# elif a == b:
#     print("draw")
# else:
#     print("only rock, paper and scissors!")

#-----

# rps = ["rock", "paper", "scissors"]

# if (a in rps) and (b in rps):
#     if a == b:
#         print("draw")
#     elif (a == rps[0] and b == rps[2]) or (a == rps[1] and b == rps[0]) or (a == rps[2] and b == rps[1]):
#         print("player1 win")
#     else:
#         print("player2 win")
# else:
#     print("only rock, paper and scissors!")

#-----

# p1_win = [("rock"+"scissors"),("paper"+"rock"),("scissors"+"paper")]

# if (a in rps) and (b in rps):
#     if a == b:
#         print("draw")
#     elif (a+b) in p1_win:
#         print("player1 win")
#     else:
#         print("player2 win")
# else:
#     print("only rock, paper and scissors!")

rps = ["rock", "paper", "scissors"]
p1_win = [("rock"+"scissors"),("paper"+"rock"),("scissors"+"paper")]

p1 = 0
p2 = 0

for i in range():
    a = input("player1: rock, paper or scissors? = ").lower().strip()
    b = input("player2: rock, paper or scissors? = ").lower().strip()
    if (a in rps) and (b in rps):
        if a == b:
            if (a+b) in p1_win:
                print(f"player1 : {p1 + 1}")
                
            else:
                print(f"player2 win : {p2 + 1}")

            if (p1 == 3):
                print("player1 win")
    else:
        print("only rock, paper and scissors!")




# a = int(input("enter your number: "))
# #นับเศษ ถ้าถึง 2 จะหยุด
# nub = 0

# for i in range(1,a+1,1):
#     if a % i == 0:
#         nub = nub + 1

# if nub == 2:
#     print("prime number")
# else:
#     print("not prime")