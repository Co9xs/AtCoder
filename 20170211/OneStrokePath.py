import itertools
import numpy
N, M = map(int, input().split())
hen_list = []
for i in range(M):
  a, b = map(int, input().split())
  hen_list.append([a,b]) #2頂点で1つの辺とみなすリストを作成
 
p = itertools.permutations(numpy.arange(1,N+1)) #N個の頂点から考えられる順列を列挙
ans = 0
 
for v in p:
  if list(v)[0] == 1: #その順列が1から始まっているときだけ考える
    check = [False]*(N-1) #その順列の隣り合う要素に辺があるかを記録する配列
    for i in range(N):#順列の隣り合う要素を列挙する
      if sorted(list(v)[i:i+2]) in hen_list: #隣り合う要素に辺があるかをチェック
        check[i] = True #辺があればフラグを立てる
    if all(check):
      ans += 1
print(ans)
