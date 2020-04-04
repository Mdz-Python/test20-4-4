#!/usr/bin/env python3
sticks = 21

print("有21根棍子，每次只能拿1-4根")
print("谁拿到最后一根谁输")

while True:
    print("棍子数量：",sticks)
    if sticks == 1:
        print("你拿到最后一根你就输了")
        break
    sticks_taken = int(input("要拿的棍子数:"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took:",(5-sticks_taken),"\n")
    sticks -= 5
