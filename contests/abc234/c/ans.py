# 受け取った整数を2進数表記の文字列に変換して、"0b"のprefixを削除し、1を2に書き換える
print(bin(int(input()))[2:].replace("1", "2"))
