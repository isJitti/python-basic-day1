# Warm-up while loop
hello = 1
while hello <= 5:
    print(hello)
    hello = hello + 1

# Warm-up 2 (while-loop)
greet = 1
while greet <= 7:
    print("Hello Python")
    greet = greet + 1

# ระบบถามชื่อซ้ำจนกว่าผู้ใช้จะพิมพ์ชื่อถูก
correct = "jittipat"
guess = input("ทายชื่อมาหน่อย :")
while guess != correct:
    print("ตอบผิด")
    guess = input("ทายอีก")
if correct == guess:
    print("ถูกต้องงงงงงงงง !!!")
else:
    print("ตอบผิด")
