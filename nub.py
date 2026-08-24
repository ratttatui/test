a = "110235120"
nub0 = 0
nub1 = 0
nub2 = 0
nub3 = 0
nub4 = 0
nub5 = 0

for i in a:
    if i == "0":
        nub0 = nub0+1
    elif i == "1":
        nub1 = nub1+1
    elif i == "2":
        nub2 = nub2+1
    elif i == "3":
        nub3 = nub3+1
    elif i == "4":
        nub4 = nub4+1
    elif i == "5":
        nub5 = nub5+1

print(nub0, nub1, nub2, nub3, nub4, nub5)