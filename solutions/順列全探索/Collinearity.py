import itertools
N = int(input())
exist = False
xy = [list(map(int, input().split())) for _ in range(N)]
P = itertools.permutations(xy, 3)
for p in P:
  x1, y1 = p[0]
  x2, y2 = p[1]
  x3, y3 = p[2]
  dx1 = x2 - x1
  dx2 = x3 - x1
  dy1 = y2 - y1
  dy2 = y3 - y1
  if dx2*dy1 == dx1*dy2:
    exist = True
    
if exist:
  print('Yes')
else:
  print('No')
