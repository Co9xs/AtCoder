import math
N = int(input())
pow_num_set = set() # i^jで表せる数のset
sq = math.ceil(math.sqrt(N)) # 与えられたNの範囲で基数の最大はルートNくらい

for i in range(2, sq+1): # iは基数
  for j in range(2, 34): # 2^33がN<=10^10の範囲で取りうる2乗数の最大だから33まで数えれば十分
    if 1 <= i**j <= N:
      pow_num_set.add(i**j)
    else:
      break
print(N-len(pow_num_set))
