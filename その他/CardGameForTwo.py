N = int(input())
cards_list = list(map(int, input().split()))
alice_point = 0
bob_point = 0

# カードリストがなくなるまでループ
while cards_list:
  # 最大値を求めて配列から削除してアリスのポイントに足す
  alice_turn_max = max(cards_list)
  cards_list.remove(alice_turn_max)
  alice_point += alice_turn_max
  
  # アリスのターンでカードがなくなることを考慮
  if cards_list:
    # その後に最大値を求めて配列から削除してボブのポイントに足す
    bob_turn_max = max(cards_list)
    cards_list.remove(bob_turn_max)
    bob_point += bob_turn_max

diff = alice_point - bob_point
print(diff)
