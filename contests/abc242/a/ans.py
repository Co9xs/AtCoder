a, b, c, x = map(int, input().split())
ans = 0
# a位以上ならかならずもらえる
if x <= a:
  ans = 1
if a < x <= b:
  ans = c / (b-a)
if x > b:
  ans = 0
print("{:.012f}".format(ans))
