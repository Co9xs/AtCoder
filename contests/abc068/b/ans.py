n = int(input())
max_count = 0
ans = 1

for i in range(1, n+1):
  temp_count = 0
  s = i
  while s % 2 == 0:
    temp_count += 1
    s = s / 2
  if temp_count > max_count:
    max_count = temp_count
    ans = i

print(ans)


