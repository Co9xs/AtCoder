import math


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
  for j in range(i+1, N):
    temp = 0
    for d in range(D):
      temp += (X[i][d] - X[j][d])*(X[i][d] - X[j][d])
    if math.sqrt(temp).is_integer():
      ans += 1
      
print(ans)

