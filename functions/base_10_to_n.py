# 10進数表記の整数をn進数表記に変換する
def base_10_to_n(x, n):
  out = ""
  while(x > 0):
   out =  str(x % n) + out
   x = int(x/n)
  return out
