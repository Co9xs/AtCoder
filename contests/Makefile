include .env

default:
	echo noop

# コンテストIDディレクトリを作成
new:
	acc new ${CONTEST_ID}

# 問題を追加
add:
	cd ${CONTEST_ID} && acc add

# 問題ディレクトリ配下に回答用のファイルを作成して開く
solve-%:
	cd ${CONTEST_ID}/${@:solve-%=%} && touch ans.${EXT} && open ans.${EXT}

submit-%:
	cd ${CONTEST_ID}/${@:submit-%=%} && acc s ans.py

# 回答用ファイルに対してテストケースを実行
test-%:
	cd ${CONTEST_ID}/${@:test-%=%} && oj t -c "${LANG} ./ans.${EXT}" -d ./tests/
