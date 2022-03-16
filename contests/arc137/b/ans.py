import itertools

n = int(input())
a = list(map(int, input().split()))

def t(l, x):
  nl = [list(b) for a,b in itertools.groupby(l)]
  m = 0
  for ll in nl:
    if (ll[0] == x):
      m = max(m, len(ll))
  return m

def main():
  # ±0 という結果が必ず取れるので最小でも1通り
  ans = 1
  # 全部 1 のとき or 全部 0 のときは配列の長さの分だけ -x or +x することができる
  if all(a) or not any(a):
    ans += len(a)
  else:
    # それ以外のとき(0と1が両方含まれるとき)は+1, -1が必ずできるので2通り
    ans += 2
    # 0 or 1が2つ以上連続している場合は(連続している個数-1)通りが新たにできる
    if (t(a, 0) >= 2):
      ans += t(a, 0) -1
    if (t(a, 1) >= 2):
      ans += t(a, 1) - 1
  
  print(ans)

main()
# print(t(a, 0), t(a, 1))
