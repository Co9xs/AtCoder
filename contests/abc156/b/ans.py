def base_10_to_n(x, n):
  out = ""
  while(x > 0):
   out =  str(x % n) + out
   x = int(x/n)
  return out

def main():
  n, k = map(int, input().split())
  n_str = str(base_10_to_n(n,k))
  print(len(n_str))

main()
