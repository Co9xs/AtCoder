n, a, b = map(int, input().split())

def degitSum(n):
  s = str(n)
  array = list(map(int, s))
  return sum(array)

def main():
  sum = 0
  for i in range(n+1):
    if (a <= degitSum(i) and degitSum(i) <= b):
      sum += i
  print(sum)

main()
