N = int(input())
A = list(map(int, input().split()))
colors = {
  "gray": 0,
  "brown": 0,
  "green": 0,
  "light_blue": 0,
  "blue": 0,
  "yellow": 0,
  "orange": 0,
  "red": 0,
}
over_3200 = 0

for a in A:
  if (1 <= a <= 399):
    colors["gray"] += 1
  elif (400 <= a <= 799):
    colors["brown"] += 1
  elif (800 <= a <= 1199):
    colors["green"] += 1
  elif (1200 <= a <= 1599):
    colors["light_blue"] += 1
  elif (1600 <= a <= 1999):
    colors["blue"] += 1
  elif (2000 <= a <= 2399):
    colors["yellow"] += 1
  elif (2400 <= a <= 2799):
    colors["orange"] += 1
  elif (2800 <= a <= 3199):
    colors["red"] += 1
  else:
    over_3200 += 1

count = 0
# 基本的には色の種類数が最小になる
for k, v in colors.items():
  if colors[k] > 0:
    count += 1

# 例外として色の種類数が0のとき(全員が3200人以上のとき)は最小は1
if (count == 0):
  print(1, over_3200)
# 色の種類に3200以上の人数を足した数が最大になる
else:
  print(count, count+over_3200)
