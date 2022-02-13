n = int(input())

def main():
  d = []
  for _ in range(n):
    d.append(int(input()))
  d = list(set(d))
  print(len(d)) 

main()
