from math import sqrt

def main():
  n = int(input())
  x = [0]*n
  y = [0]*n

  for i in range(n):
    x[i], y[i] = map(int, input().split())

  ans = 0
  for i in range(n):
    for j in range(n):
      dx = x[i] - x[j]
      dy = y[i] - y[j]
      ans = max(ans, sqrt(dx**2 + dy**2)) 
  print(ans)

main()
