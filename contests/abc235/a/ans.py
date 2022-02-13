a, b, c = list(map(int, input()))

abc = a*100 + b*10 + c
bca = b*100 + c*10 + a
cab = c*100 + a*10 + b

print(abc+bca+cab)
