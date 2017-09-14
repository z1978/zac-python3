'''
Created on 2017年9月14日

@author: zac
'''
# 日付処理、ディレクトリ処理で利用
import datetime
import os
# 一定時間の待ちを入れるために利用
import time
import GetHtml

# 日付のディレクトリがなければ作成する
today = datetime.date.today()
dirname = today.strftime('%Y%m%d')
if not os.path.exists(dirname):
    os.mkdir(dirname)
#start_url = 'http://resource.pcassist.co.jp/sozai/IT56/chapter13/sample13_3_2.html'
start_url = 'http://shop.zhongyeyuan.com.cn/'

if __name__ == '__main__':
    print("----- Zac START -----")
    GetHtml.get_html(start_url, dirname)
    print("----- Zac END -----")
