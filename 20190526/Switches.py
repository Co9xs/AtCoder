# N個のスイッチのon/offの組み合わせは2^N通り→bit全探索
# 2進数N桁の数でどこか1になっているのかをチェックして配列に記録
N, M = map(int, input().split())
bulbs = [list(map(int, input().split()))[1:] for _ in range(M)]
p = list(map(int, input().split()))
ans = 0
for switches in range(2**N): #switchsは2^N通りを2進数で動く
  check = [False]*M #電球がついているかどうかの配列
  for i, bulb in enumerate(bulbs): #すべての電球に対して動く
    on_count = 0 #電球につながっているスイッチの中でonをカウントする変数
    for connected_switch in bulb:
      if switches>>(connected_switch-1)&1:
        on_count+=1
    if on_count % 2 == p[i]:
      check[i] = True
    else:
      check[i] = False
  if all(check):
    ans += 1
print(ans)
