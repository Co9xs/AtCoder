n = int(input())
a_list = list(map(int, input().split()))

# 切れ込み位置のリスト（0°, 360°, には最初から切れ込みが入っている）
b_list = [0, 360]

sum = 0
# 反時計周りにA1°, (A1°+A2°)%360°, (A1°+A2°+A3°)%360°, ・・・と切れ込みが入っていく
for i in range(n):
  sum += a_list[i]
  sum %= 360
  b_list.append(sum)

# 切れ込み位置のリストを昇順でソート
b_list.sort()

ans = 0
# 切れ込み位置のリストは最大でも長さN+2
for i in range(n+1):
  ans = max(ans, b_list[i+1] - b_list[i])
print(ans)
