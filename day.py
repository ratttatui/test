# เช็ควันหยุด: ถ้าเป็นวันเสาร์ หรือ อาทิตย์ พิมพ์ “วันหยุด” ไม่งั้น “วันทำงาน”

day = input("What day is it?: ").lower().strip()

if day in ("saturday", "sat", "sunday", "sun"):
    print("It's Weekend!🥳⛱️🎉🌞")
elif day in ("monday","mon","tuesday","tue","wednesday","wed","thursday","thu","friday","fri"):
    print("It's Weekday...😢💔💼🥀")
else:
    print("🤨❓")

