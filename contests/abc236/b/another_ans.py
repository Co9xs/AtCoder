from calendar import c


n = int(input())
a_list = list(map(int, input().split()))
count = [0] * n

for a in a_list:
  count[a-1] += 1

for i in range(n):
  if count[i] == 3:
    print(i+1)

