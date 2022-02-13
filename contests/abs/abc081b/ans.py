n = int(input())
a = list(map(int, input().split()))

def main():
  count = 0
  while(True):
    exist_odd = False
    for i in range(n):
      if a[i] % 2 != 0:
        exist_odd = True
    if exist_odd:
      break
    for i in range(n):
      a[i] /= 2
    count += 1
  print(count)

main()
