# AtCoder
## 概要
AtCoder練習用レポジトリ

アルゴリズム練習のためAtCoderでAcceptがついたコードをまとめていく

言語は組み込み関数の充実度と文法の簡単さからPythonを選択する

初心者のためA〜C問題を中心に解いていく

## acc, ojをつかった提出までの流れ
### コンテストIDの取得

AtCoderのURLの`/content/`以下でコンテストIDを取得

ex. https://atcoder.jp/contests/abc239 であれば `abc239`がコンテストID


### コンテストごとのディレクトリを作成

`/atcoder/contests/`配下で`acc new コンテストID`を実行すると、問題用のディレクトリが作成される

問題用ディレクトリ内に回答用ファイル`ans.py`を作成する


### テストケースの実行

問題用ディレクトリ内で`oj t -c "python3 ./ans.py" -d ./tests/`を実行


### コードの提出

問題用ディレクトリ内で`acc s ans.py`で提出ページが開く


### 問題用ディレクトリの追加

コンテスト用ディレクトリの配下で`acc add`を実行し、問題を選択してEnterで追加可能
