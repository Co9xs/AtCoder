h, w = map(int, input().split())
# 行列を作成
b = [list(map(int, input().split())) for _ in range(h)]

# 1列ごとにb[j][i]をlistにいれてprintする
for i in range(w):
  lis = []
  for j in range(h):
    lis.append(b[j][i])
  print(*lis)
