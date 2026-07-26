print("Buy 3 Items:")
a = input("1. ").lower()
b = input("2. ").lower()
c = input("3. ").lower()

#____________

if a == "bottle" or a == "water bottle":
    price1 = 10.0
elif a == "pencil":
    price1 = 5.0
elif a == "paper":
    price1 = 3.0
elif a != "bottle" and a != "water bottle" and a != "pencil" and a != "paper":
    price1 = 0.0

#____________

if b == "bottle" or b == "water bottle":
    price2 = 10.0
elif b == "pencil":
    price2 = 5.0
elif b == "paper":
    price2 = 3.0
elif b != "bottle" and b != "water bottle" and b != "pencil" and b != "paper":
    price2 = 0

#____________

if c == "bottle" or c == "water bottle":
    price3 = 10.0
elif c == "pencil":
    price3 = 5.0
elif c == "paper":
    price3 = 3.0
elif c != "bottle" and c != "water bottle" and c != "pencil" and c != "paper":
    price3 = 0

#_____________

if price1 == 0 and a!= "":
    print("Sorry! We don't have", a.capitalize(),"(ᴗ_ᴗ.)")
if price2 == 0 and b!= "":
    print("Sorry! We don't have", b.capitalize(),"(ᴗ_ᴗ.)")
if price3 == 0 and c!= "":
    print("Sorry! We don't have", c.capitalize(),"(ᴗ_ᴗ.)")

#_____________

subtotal = price1+price2+price3
vat = round(subtotal*0.07, 2)

#____________receipt

if (price1 + price2 + price3) > 0:
    print("╔"+("═"*26)+"╗")
    print("║".ljust(2),"⋆ ˚｡⋆୨୧˚"+"\033[1m"+"Receipt"+"\033[0m"+"˚୨୧⋆｡˚ ⋆".ljust(5),"║")
    print("║".ljust(3),("︶"*10).ljust(12),"║")
    print("║".ljust(3),"\033[4m"+"Item"+"\033[0m".ljust(15)+"\033[4m"+"Price"+"\033[0m".ljust(6),"║")

# ____________item1

    if price1 > 0:
        print("║".ljust(3),a.ljust(15).capitalize()+("฿"+str(price1)).ljust(7),"║")

# ____________item2

    if price2 > 0:
        print("║".ljust(3),b.ljust(15).capitalize()+("฿"+str(price2)).ljust(7),"║")


# ____________item3

    if price3 > 0:
        print("║".ljust(3),c.ljust(15).capitalize()+("฿"+str(price3)).ljust(7),"║")

# ____________subtotal

    print("║".ljust(3),("-"*20).ljust(22),"║")
    print("║".ljust(3),"Sub Total:".ljust(14),("฿"+str(subtotal)).ljust(7),"║")

# ____________vat

    print("║".ljust(3),"Vat 7%:".ljust(14),("฿"+str(vat)).ljust(7),"║")

# ____________total

    print("║".ljust(3),("-"*20).ljust(22),"║")
    print("║".ljust(3),"Total:".ljust(14),("฿"+ str(subtotal+vat)).ljust(7),"║",)
    print("║".ljust(3),("︶"*10).ljust(12),"║")
    print("║".ljust(4),"Thank you!(^ᴗ^ )~*".ljust(21),"║")
    print("╚"+("═"*26)+"╝")