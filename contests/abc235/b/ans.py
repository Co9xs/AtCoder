N = int(input())
H = list(map(int, input().split()))
position = 0

while position+1 < N and H[position]<H[position+1]:
  position += 1

print(H[position])
