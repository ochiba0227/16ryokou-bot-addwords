# -*- coding: utf-8 -*-

import os
import datetime
import random
import json
import MySQLdb

from bottle import route, run, debug, template, request, static_file, auth_basic

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH = BASE_DIR + "/views"
# coffeeスクリプトを配置するパスを指定
COFFEE_PATH = os.environ.get("COFFEE_PATH")

source_str = 'abcdefghijklmnopqrstuvwxyz'

#connector = MySQLdb.connect(host="localhost", db="BOT", user="root", charset="utf8")
connector = MySQLdb.connect(host="localhost", db="BOT", user="root", passwd="summer", charset="utf8")

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
    print json.dumps(result)
    cursor.close()
    return template(TEMPLATE_PATH+'/show', result=json.dumps(result))

def make_script(call,response):
    todayDate = datetime.datetime.today()
    randstr = "".join([random.choice(source_str) for x in xrange(5)])
    filename = "{0}-{1}.coffee".format(todayDate.strftime("%Y%m%d%H%M%S"),randstr)

    # 話しかける言葉のリスト
    call_list = split_text(replace_reg(call))
    if(len(call_list)==0):
        return 'error'

    # 返事のリスト
    response_list = split_text(replace_reg(response))
    if(len(response_list)==0):
        return 'error'

    # 話しかける言葉（スクリプト用）
    call = '|'.join(call_list)

    # 返事（スクリプト用）
    length = len(response_list)
    response = 'msg.random ['
    for i in range(length):
        response = response + '"' + response_list[i] + '"'
        if(i<length-1):
            response = response + ','
    response = response + ']'

    writer = open(os.path.join(COFFEE_PATH,filename),'w')
    writer.write('module.exports = (robot) ->\n')
    writer.write('\trobot.hear /^@16ryokou-bot.*({0}).*/i, (msg) ->\n \t\tmsg.send {1}\n \t\tmsg.finish()\n'.format(call,response))
    writer.close()

    write_db(call_list,",".join(response_list),filename)
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
def write_db(call_list,response,filename):
    cursor = connector.cursor()
    for call in call_list:
        sql = 'insert into BOT.WORDS values("{0}","{1}","{2}")'.format(call,response,filename)
        cursor.execute(sql)
    # ここで書き込まれる
    connector.commit()
    cursor.close()

run(host='localhost', port=9000)
