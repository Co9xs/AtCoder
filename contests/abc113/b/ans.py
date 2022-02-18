N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

def mean_temp(x):
  return T - (int(x) * 0.006)

def main():
  most_near = 600
  ans = 0

  for i in range(N):
    mean = mean_temp(H[i])
    current = abs(A - mean)
    if current < most_near:
      most_near = current
      ans = i+1
  
  print(ans)

main()
