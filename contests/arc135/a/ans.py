import math

def main():
  l  = [int(input())]
  MOD = 998244353

  # 最初の整数が4以下のときはそれがそのまま答え
  ans = l[0] if l[0] <= 4 else 1

  # 最大値が4以下になった時点でループを抜ける(分解できる5以上の整数が存在しないので)
  while (l[-1] > 4):
    # 現状の最大値を保持
    temp_max = l[-1]

    # 最大値/2を切り捨て、切り上げに分解する
    f = math.floor(temp_max/2)
    c = math.ceil(temp_max/2)

    # 分解後の値が4以下の場合はこれ以上分解されないので答えにかけておく
    if f <= 4:
      ans *= f
      ans %= MOD
    if c <= 4:
      ans *= c
      ans %= MOD

    # 分解したものをリストに追加
    l.append(f)
    l.append(c)
    # 分解した元の整数はリストから削除する
    l.sort()
    l.pop()
  
  print(ans)

main()
