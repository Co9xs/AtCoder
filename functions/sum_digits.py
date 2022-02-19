# 整数の各桁の和を求める関数
def sum_digits(n):
  res = 0
  while (n > 0):
    res += n % 10
    n //= 10
  return res

