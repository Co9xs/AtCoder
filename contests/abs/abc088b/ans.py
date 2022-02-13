n = int(input())
a = list(map(int, input().split()))

def pickTheMax(l):
  point = max(l)
  l.remove(point)
  return point

def main():
  alice = 0
  bob = 0
  while (len(a) > 0):
    alice += pickTheMax(a)
    if (len(a) > 0):
      bob += pickTheMax(a)
  print(alice - bob)

main()
