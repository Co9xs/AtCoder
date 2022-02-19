a, b, c, d = map(int, input().split())

def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for p in range(2, n):
      if n % p == 0:
        return False
  return True

for i in range(a, b+1):
  l = []
  for j in range(c, d+1):
    l.append(isPrime(i+j))
  # a以上b以下の整数iに対して和が素数になるようなjがひとつも存在しないなら先手のTakahashiくんが必勝（そのiを選べば良いので）
  if not any(l):
    print("Takahashi")
    exit()
# そうでなければ、Takahashiくんが選んだiに対して和が素数となるようなjは存在するのでAokiくんの勝ち
print("Aoki")
