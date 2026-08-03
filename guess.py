# เกมทายเลข: กำหนดเลขลับไว้ในโค้ด (เช่น 7) รับเลขจากผู้ใช้ ถ้าทายถูกพิมพ์ “ถูกต้อง!” ถ้าน้อยไปพิมพ์ “ลองเลขที่มากกว่านี้” ถ้ามากไปพิมพ์ “ลองเลขที่น้อยกว่านี้”

from secret_number import secretnumber

num = int(input("Guess the number, 1-20: "))

if num > 20 and num < 1:
    print("Guess 1-20!!")
elif num == secretnumber:
    print("You are correct! :D")
elif num > secretnumber:
    print("Too high! Try lower!")
else:
    print("Too low! Try higher!")
