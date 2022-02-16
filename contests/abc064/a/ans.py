r, g, b = map(str, input().split())

i = int(r+g+b)
if (i % 4 == 0):
  print("YES")
else:
  print("NO")
