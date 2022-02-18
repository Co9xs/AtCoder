s = input()
l = len(s)
a = 0
b = 0

def main():
  a = 0
  b = 0
  # "A"は前から探索する
  for i in range(l):
    if s[i] == "A":
      a = i
      break
  # "Z"は後ろから探索する
  for i in range(l):
    if s[len(s)-1-i] == "Z":
      b = len(s)-1-i
      break
  # 一番うしろに近い"Z"のindex - 一番先頭に近い"A"のindex + 1で部分文字列の長さの最大値
  print(b-a+1)

main()
