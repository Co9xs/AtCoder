def main():
  n = int(input())
  can = False
  for i in range(n):
    for j in range(n):
      if 4 * i + 7 * j == n:
        can = True
        
  if can:
    print("Yes")
  else: 
    print("No")

main()
