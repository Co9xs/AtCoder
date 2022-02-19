n = int(input())

def sum_digits(n):
  res = 0
  while (n > 0):
    res += n % 10
    n //= 10
  return res

def main():
  res = 100
  for i in range(1,n):
    j = n-i
    temp = sum_digits(i) + sum_digits(j)
    res = min(res, temp)
  print(res)

main()
