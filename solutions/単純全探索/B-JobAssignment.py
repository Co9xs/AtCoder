# URL: https://atcoder.jp/contests/abc194/tasks/abc194_b

# 人数をNとする
N = int(input())

# N人の従業員のA, Bタスクにかかる時間を[[A0, B0], ..., [Ai, Bi], ..., [AN, BN]]の形で保存
times_info = [list(map(int, input().split())) for i in range(N)]

# Aタスクにかかる時間の配列
Ai_list = [times_info[i][0] for i in range(N)]
# Bタスクにかかる時間の配列
Bi_list = [times_info[i][1] for i in range(N)]
# 結果の配列
times_list = []

# 2重for文ですべての組み合わせをチェック
for i in range(N):
  for j in range(N):
    # 同じ従業員の時間から算出するときは合計値
    if i == j:
      times_list.append(Ai_list[i] + Bi_list[j])
    # 違う従業員の同士の時間から算出するときはどちらか大きい値
    else:
      times_list.append(max(Ai_list[i], Bi_list[j]))

# 結果の配列から最小を出力
print(min(times_list))
