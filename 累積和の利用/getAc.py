N, Q = map(int, input().split())
S = input()
acum = [0]*(N+1)

# 累積和の計算
for i in range(N):
  if i+1<N and S[i] == 'A' and S[i+1] == 'C':
    acum[i+1] = acum[i] + 1
  else:
    acum[i+1] = acum[i]
    
# クエリの実行
for q in range(Q):
  l, r = map(int, input().split())
  l -= 1
  r -= 1
  print(acum[r] - acum[l])
