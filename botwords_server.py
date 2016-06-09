# -*- coding: utf-8 -*-

import os
import json
import MySQLdb

from bottle import route, run, debug, template, request, static_file, auth_basic

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH = BASE_DIR + "/views"
# coffeeスクリプトを配置するパスを指定
COFFEE_PATH = os.environ.get("COFFEE_PATH")

connector = MySQLdb.connect(host="localhost", db="BOT", user="root", charset="utf8")
#connector = MySQLdb.connect(host="localhost", db="BOT", user="root", passwd="summer", charset="utf8")

# BASIC認証のユーザ名とパスワード
USERNAME = "16shinsotsu"
PASSWORD = "16shinsotsu"


def check(username, password):
    return username == USERNAME and password == PASSWORD

@route('/botwords/css/<filename>')
def css_dir(filename):
    return static_file(filename, root=BASE_DIR+"/static/css")

@route('/botwords/js/<filename>')
def js_dir(filename):
    return static_file(filename, root=BASE_DIR+"/static/js")

@route('/botwords/img/<filename>')
def img_dir(filename):
    return static_file(filename, root=BASE_DIR+"/static/img")

@route('/botwords/font/<filename>')
def font_dir(filename):
    return static_file(filename, root=BASE_DIR+"/static/fonts")

@route('/botwords')
def index():
  return template(TEMPLATE_PATH+'/index')

@route('/botwords', method='POST')
def add_word():
    call = request.forms.get('call')
    response = request.forms.get('response')
    flag = make_script(call,response)
    return flag

@route('/botwords/show')
@auth_basic(check)
def show_db():
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM BOT.WORDS")
    result = cursor.fetchall()
    cursor.close()
    return template(TEMPLATE_PATH+'/show', result=json.dumps(result))

def make_script(call,response):
    # 話しかける言葉のリスト
    call_list = split_text(replace_reg(call))
    if(len(call_list)==0):
        return 'error'

    # 返事のリスト
    response_list = split_text(replace_reg(response))
    if(len(response_list)==0):
        return 'error'

    # DBへ書き込み&ファイル書き出し
    write_words(call_list,response_list)

    return ''

# 分割し、空白を捨てて、リスト型を返す
def split_text(text):
    split_list = text.split('|')

    while split_list.count('') > 0:
        split_list.remove('')

    return split_list;

# 正規表現な文字のエスケープ
def replace_reg(text):
    text = text.replace('*', '\*')
    text = text.replace('+', '\+')
    text = text.replace('^', '\^')
    text = text.replace('$', '\$')
    text = text.replace('.', '\.')
    text = text.replace('{', '\{')
    text = text.replace('}', '\}')
    text = text.replace('[', '\[')
    text = text.replace(']', '\]')
    text = text.replace('(', '\(')
    text = text.replace(')', '\)')
    return text;

# DBへ書き込み
def write_words(call_list,response_list):
    cursor = connector.cursor()
    for call in call_list:
        for response in response_list:
            cursor.execute('select RESPONSE_WORD from BOT.WORDS where CALL_WORD = "{0}" and RESPONSE_WORD = "{1}"'.format(call,response))
            words = cursor.fetchall()
            # 言葉の組が存在しなければ追加
            if(len(words)==0):
                sql = 'insert into BOT.WORDS (CALL_WORD,RESPONSE_WORD) values("{0}","{1}")'.format(call,response)
                cursor.execute(sql)
                # ここでDBへ書き込まれる
                connector.commit()
        # ファイル書き出し
        words_to_file(call)
    cursor.close()

# ファイルへ書き出し
def words_to_file(call):
    # 話しかけた言葉に対してbotがしゃべる言葉をDBから取得
    cursor = connector.cursor()
    cursor.execute('select ID,RESPONSE_WORD from BOT.WORDS where CALL_WORD = "{0}"'.format(call))
    words = cursor.fetchall()
    cursor.close()

    # ファイル名は一番上のid
    filename = '{0}.coffee'.format(words[0][0])

    # ファイル書き込み準備
    response = '['
    length = len(words)
    for i in range(length):
        response = response + '"{0}"'.format(words[i][1].encode('utf-8'))
        if(i<length-1):
            response = response + ','
    response = response + ']'

    writer = open(os.path.join(COFFEE_PATH,filename),'w')
    writer.write('# Commands:\n')
    writer.write('# hubot {0}\n'.format(call))
    writer.write('module.exports = (robot) ->\n')
    writer.write('\trobot.respond /{0}$/i, (msg) ->\n \t\tmsg.send msg.random {1}\n \t\tmsg.finish()\n'.format(call,response))
    writer.close()

run(host='localhost', port=9000)
