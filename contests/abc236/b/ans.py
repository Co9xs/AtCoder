n = int(input())
a_list = list(map(int, input().split()))
default_sum = 0
final_sum = 0

for i in range(n):
  default_sum += 4 * (i+1)

for e in a_list:
  final_sum += e

print(default_sum - final_sum)
