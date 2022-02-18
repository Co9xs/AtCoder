import math
def main():
  n, x = map(int, input().split())
  # 必ずn種類を1個づつは作れる
  ans = n
  # お菓子の素の必要量は最大でも1000
  min_d = 1000

  # n種類のお菓子を一つづつ作成していく
  for _ in range(n):
    m = int(input())
    # 最小値を保存しておく
    min_d = min(min_d, m)
    x -= m

  # n種類を1個づつ作ったあとに残ったxを最小値で割る
  ans += math.floor(x / min_d)
  print(ans)

main()
