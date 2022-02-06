n = int(input())

# ある程度nが大きければ 2**n > n*n となるのは見当がつくのでその閾値を求める
if (2 <= n and n <= 4):
  print("No")
else:
  print("Yes")
