'''
Created on 2017年9月14日

@author: zac
'''
  # coding: utf-8

# Webからの取得、HTML解析で利用
import requests
from bs4 import BeautifulSoup
# 日付処理、ディレクトリ処理で利用
import datetime
import os
# 一定時間の待ちを入れるために利用
import time

def get_html(url, dirname):
    # 負荷をかけないように時間を空ける
    time.sleep(1)
    # 処理状況がわかるように表示
    print('Process {}'.format(url))
    # 指定されたURLの取得
    response = requests.get(url)
    response.encoding = 'utf-8'
    # リンクされている各ファイルについて再帰処理
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        get_html(href, dirname)
    # 取得したHTMLをファイルとして保存
    # ファイル名を取得（/で区切った最後の要素がファイル名）
    filename = url.split('/')[-1]
    # 指定されたディレクトリと連結してファイルパスにする
    filepath = os.path.join(dirname, filename)
    # 文字エンコーディングを指定しないとWindowsではShift-JISで保存されるので注意
    # また、newline引数で空文字列を指定しないと改行がされすぎることがある
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(response.text)
# 日付のディレクトリがなければ作成する
# today = datetime.date.today()
# dirname = today.strftime('%Y%m%d')
# if not os.path.exists(dirname):
#     os.mkdir(dirname)
#
# start_url = 'http://resource.pcassist.co.jp/sozai/IT56/chapter13/sample13_3_2.html'
# get_html(start_url, dirname)
