n = int(input())
s = input()

for i in range(n):
  # 1文字先読みして見ていくと、出てくる可能性のある2文字は[AA, BB, CC, AB, BA, BC, CB, AC, CA]の9種類
  # そのうち与えられたの変換を行って辞書順を早くできるのは、BB→A と BA→BBB→ABの変換のみ

  if (s[i:i+2] == "BB"):
    s = s[0:i] + "A" + s[i+2:len(s)]
  if (s[i:i+2] == "BA"):
    s = s[0:i] + "AB" + s[i+2:len(s)]

print(s)
