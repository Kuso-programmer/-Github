import random

print("🎮 数当てゲーム 🎮")
print("=================")

answer = random.randint(1, 10)

for i in range(3):
    print(i + 1, "回目")
    num = int(input("1〜10の数字を入れてね："))

    if num == answer:
        print("正解！！🎉")
        break
    elif num > answer:
        print("ちがうよ")
        print("ヒント:もっと小さい")
    else:
        print("ちがうよ")
        print("ヒント:もっと大きい")

print("答えは", answer)

