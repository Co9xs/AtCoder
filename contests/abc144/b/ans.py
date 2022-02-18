n = int(input())

def solve():
  for i in range(1, 10):
    for j in range(1, 10):
      if i * j == n:
        return True
  return False

def main():
  can = solve()
  if (can):
    print("Yes")
  else:
    print("No")

main()
