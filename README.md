# AtCoder
## 概要
AtCoder練習用レポジトリ

アルゴリズム練習のためAtCoderでAcceptがついたコードをまとめていく

言語は組み込み関数の充実度と文法の簡単さからPythonを選択する

初心者のためA〜C問題を中心に解いていく
## Makefileのコマンド一覧
※新しいコンテストに参加するたびに`contests/.env`のCONTEST_IDを設定する
|  コマンド  |  実行結果  |
| ---- | ---- |
|  `make new`  |  環境変数CONTEST_IDを読み込んで`./contests`配下に新しいコンテストを作成します  |
|  `make add`  |  `./contests/CONTEST_ID`ディレクトリ配下に問題ディレクトリ(ex: ./a, ./b)を作成します  |
|  `make solve-hoge`  |  `./contests/CONTEST_ID/hoge`ディレクトリ配下にans.pyを作成して開きます  |
|  `make test-hoge`  | `./contests/CONTEST_ID/hoge/ans.py`に対して`./contests/CONTEST_ID/hoge/tests`のテストケースを実行します |
