n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# そもそも配列の要素は同じでなければ実現不可能
if sorted(a) != sorted(b):
  print("No")
  exit()

for j in range(0, n-2):
  sub_b = int(str(b[j]) + str(b[j+1]) + str(b[j+2]))
  bool_map = [0] * int(n-2)
  for i in range(0, n-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    xyz = int(str(x) + str(y) + str(z))
    xzy = int(str(x) + str(z) + str(y))
    yxz = int(str(y) + str(x) + str(z))
    yzx = int(str(y) + str(z) + str(x))
    zxy = int(str(z) + str(x) + str(y))
    zyx = int(str(z) + str(y) + str(x))

    # 一つでも同じ数字があればxyzからなる順列はすべて実現可能
    if (x == y or  y == z or x == z):
      if (sub_b == xyz or sub_b == xzy or sub_b == yxz or sub_b == yzx or sub_b == zxy or sub_b == zyx):
        bool_map[i] = 1
      else:
        bool_map[i] = 0
    else:
      if (sub_b == xyz or sub_b == zxy or sub_b == yzx):
        bool_map[i] = 1
      else:
        bool_map[i] = 0

  if not any(bool_map):
    print("No")
    exit()
print("Yes")


