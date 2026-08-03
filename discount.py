# ระบบส่วนลด: ถ้าซื้อของ >= 1000 บาท ลด 10%, >= 500 ลด 5%, น้อยกว่านั้นไม่ลด แล้วพิมพ์ราคาสุทธิ


#### Fast Food


price = int(input("How much do you spend?: "))

discount1 = price-(price*0.1)
discount2 = price-(price*0.05)

if price >= 1000:
    print(f"You got 10% discount! Your total price is {discount1} !")
elif price >= 500:
    print(f"You got 5% discount! Your total price is {discount2} !")
else:
    print(f"Your total price is {price} !")


#### Fine Dining 



price = int(input("How much do you spend?: "))


if price >= 1000:
    discount1 = price-(price*0.1)
    print(f"You got 10% discount! Your total price is {discount1} !")
elif price >= 500:
    discount2 = price-(price*0.05)
    print(f"You got 5% discount! Your total price is {discount2} !")
else:
    print(f"Your total price is {price} !")