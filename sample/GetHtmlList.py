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
        if href not in href_list:
            href_list.append(href)
            get_html(href, dirname)

# 日付のディレクトリがなければ作成する
today = datetime.date.today()
dirname = today.strftime('%Y%m%d')
if not os.path.exists(dirname):
    os.mkdir(dirname)

#start_url = 'http://resource.pcassist.co.jp/sozai/IT56/chapter13/sample13_3_2.html'
start_url = 'https://search.yahoo.co.jp/image/search?p=Apple&ei=UTF-8&fr=top_ga1_sa'
href_list = ['#', '/', start_url]
get_html(start_url, dirname)
print(len(href_list))
print(href_list)
filepath = os.path.join(dirname, "mylist.txt")
# 文字エンコーディングを指定しないとWindowsではShift-JISで保存されるので注意
# また、newline引数で空文字列を指定しないと改行がされすぎることがある
#str1 = ''.join(href_list)
with open(filepath, 'w', encoding='utf-8', newline='') as f:
    for line in href_list:
        f.write(line + "\n" )










