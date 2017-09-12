'''
Created on 2017年9月11日

@author: zac
'''
import sys
from datetime import datetime
import sample.yahoo_img as getimg
#-*- coding:utf-8 -*-
print("----- TEST START -----" + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))



url = "https://search.yahoo.co.jp/image/search?p=Apple&ei=UTF-8&fr=top_ga1_sa"
kzm =".jpg,.gif,.jpeg,.png"
extensions = kzm.split(",")
getimg.crawring(url, extensions)

print("----- TEST END -----" + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
