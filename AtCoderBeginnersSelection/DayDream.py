S = input()
D = 'dream'
DR = 'dreamer'
E = 'erase'
ER = 'eraser'
 
# すべての文字列を反転させる
S = S[::-1]
D = D[::-1] # 'maerd'
DR = DR[::-1] # 'remaerd'
E = E[::-1]  # 'esare'
ER = ER[::-1] # 'resare'
T = ''
 
while True:
  if(S==T):
    print('YES')
    exit()
  elif(S.startswith(T+D)):
    keyword=D
  elif(S.startswith(T+DR)):
    keyword=DR
  elif(S.startswith(T+E)):
    keyword=E
  elif(S.startswith(T+ER)):
    keyword=ER
  else:
    print('NO')
    exit()
  T += keyword
