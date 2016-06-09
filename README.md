# ボットに喋らせる言葉の自動生成
入力された言葉を自動的にBotに追加します。

## pip集
```
pip install bottle
pip install MySQL-python
```

## 入力内容はmysqlへ記録
```
mysql> CREATE DATABASE BOT CHARACTER SET utf8;
mysql> CREATE TABLE BOT.WORDS(ID INT AUTO_INCREMENT, CALL_WORD TEXT, RESPONSE_WORD TEXT, PRIMARY KEY(ID));
```

出力されるファイル名はそのまま

## 環境変数の設定
```
export COFFEE_PATH=hubotのcoffee scriptを置いているパス
```
