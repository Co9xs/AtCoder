N = input()
D = len(N)
ans = len(N)
if int(N)%3 == 0:
  print(0)
  exit()

for i in range(2**D):
  num = 0
  cnt = 0
  for j in range(D):
    if (i>>j) & 1:
      num += int(N[j]) #j桁目に1が立っていたらnumに残す数を記録していく
      cnt += 1 #何桁残すか
    if num % 3 == 0:
      ans = min(ans, D-cnt)#D-cnt(=何桁消したか)で答えを更新していく

if ans == D:
  print(-1)
else:
  print(ans)
