# URL: https://atcoder.jp/contests/abc194/tasks/abc194_a

# 標準入力(n, m)をA, Bの形で取得
A, B = list(map(int, input().split()))

# 乳固形分
solid = A + B
# 乳脂肪分
fat = B

# あとは条件分岐で出力するだけ
if solid >= 15 and fat >=8:
  print(1)
elif solid >=10 and fat >= 3:
  print(2)
elif solid >= 3:
  print(3)
else:
  print(4)
