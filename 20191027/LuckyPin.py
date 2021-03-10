N = int(input())
S = input()
ans = []
# 決める暗証番号を000から999までの1000通りを考える
for i in range(0, 1000):
  i_zero = str(i).zfill(3) # 001のように0埋め
  p1 = S.find(i_zero[0]) # 暗証番号1桁目がSにあるかを探索して桁数をp1とする
  p2 = S.find(i_zero[1], p1+1)# S[p1+1]以降に暗証番号2桁目があるかを探索する
  p3 = S.find(i_zero[2], p2+1)# S[p2+1]以降に暗証番号3桁目があるかを探索する
  
  if p1 != -1 and p2 != -1 and p3 != -1: # すべて見つかれば暗証番号はつくれる
    ans.append(S[p1]+S[p2]+S[p3])

print(len(ans))
