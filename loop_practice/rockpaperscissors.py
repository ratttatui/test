rps = ["rock", "paper", "scissors"]
p1_win = [("rock"+"scissors"),("paper"+"rock"),("scissors"+"paper")]
sig = ['st','nd','rd']
nub_a = 0
nub_b = 0

#### repeat code
for i in range(1,4):
    a = input(f"Round {i}{sig[i-1]} player1: rock, paper or scissors? = ").lower().strip()
    b = input(f"Round {i}{sig[i-1]} player2: rock, paper or scissors? = ").lower().strip()

    if (a in rps) and (b in rps):
        if a == b:
            print("draw")
        elif (a+b) in p1_win:
            nub_a = nub_a + 1
            print(f"Round {i}{sig[i-1]} player1 win")
        else:
            nub_b = nub_b + 1
            print(f"Round {i}{sig[i-1]} player2 win")
    else:
        print("only rock, paper and scissors!")
        

print(f"P1 score : {nub_a}")
print(f"P2 score : {nub_b}")

if nub_a > nub_b:
    print("P1 is winner")
elif nub_a == nub_b:
    print("Both P draw")
else:
    print("P2 is winner")





# a = input("1st player1: rock, paper or scissors? = ").lower().strip()
# b = input("1st player2: rock, paper or scissors? = ").lower().strip()

# a = input()
# a = a.lower()
# a = a.strip()

# if (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper") or (a == "paper" and b == "rock"):
#     print("player1 win")
# elif (b == "rock" and a == "scissors") or (b == "scissors" and a == "paper") or (b == "paper" and a == "rock"):
#     print("player2 win")
# elif a == b:
#     print("draw")
# else:
#     print("only rock, paper and scissors!")

#-----

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


# if (a in rps) and (b in rps):
#     if a == b:
#         print("draw")
#     elif (a+b) in p1_win:
#         nub_a = nub_a + 1
#         print("1st round player1 win")
#     else:
#         nub_b = nub_b + 1
#         print("1st round player2 win")
# else:
#     print("only rock, paper and scissors!")

# a = input("2nd player1: rock, paper or scissors? = ").lower().strip()
# b = input("2nd player2: rock, paper or scissors? = ").lower().strip()

# if (a in rps) and (b in rps):
#     if a == b:
#         print("draw")
#     elif (a+b) in p1_win:
#         nub_a = nub_a + 1
#         print("2nd round player1 win")
#     else:
#         nub_b = nub_b + 1
#         print("2nd round player2 win")
# else:
#     print("only rock, paper and scissors!")

# a = input("3rd player1: rock, paper or scissors? = ").lower().strip()
# b = input("3rd player2: rock, paper or scissors? = ").lower().strip()

# if (a in rps) and (b in rps):
#     if a == b:
#         print("draw")
#     elif (a+b) in p1_win:
#         nub_a = nub_a + 1
#         print("3rd round player1 win")
#     else:
#         nub_b = nub_b + 1
#         print("3rd round player2 win")
# else:
#     print("only rock, paper and scissors!")