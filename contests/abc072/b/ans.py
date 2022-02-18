s = input()

def main(s):
  ans = ""
  for i in range(1, len(s)+1):
    if (i % 2 != 0):
      ans += s[i-1]
  print(ans)

main(s)
