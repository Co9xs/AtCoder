x1, y1, x2, y2 = map(int, input().split())

# 点1からの距離がroot5になる格子点の候補
list_from_1 = [
  [x1+2, y1+1],
  [x1+1, y1+2],
  [x1-1, y1+2],
  [x1-2, y1+1],
  [x1-2, y1-1],
  [x1-1, y1-2],
  [x1+1, y1-2],
  [x1+2, y1-1],
]

# 点2からの距離がroot5になる格子点の候補
list_from_2 = [
  [x2+2, y2+1],
  [x2+1, y2+2],
  [x2-1, y2+2],
  [x2-2, y2+1],
  [x2-2, y2-1],
  [x2-1, y2-2],
  [x2+1, y2-2],
  [x2+2, y2-1],
]

# それぞれの候補を探索して座標が一致する物があればOK
exist = False
for i in list_from_1:
  for j in list_from_2:
    if (i[0] == j[0] and i[1] == j[1]):
      exist = True

if (exist):
  print("Yes")
else:
  print("No")
