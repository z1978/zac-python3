#!/usr/bin/python3
import string

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'DNT': '1',
           'Host': 'www.jikexueyuan.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}

# 具体的值就不分享了，每次登录之后也是不一样的，想要那个视频的可以留言，发你邮箱
cookies = {'stat_uuid': '',
           'sensorsdata2015jssdkcross': '',
           'r_user_id': '',  # stat_fromWebUrl': '',
           'stat_ssid': '',
           'looyu_id': '',
           '_gat': '1',
           'uname': '用户名',
           'uid': '',
           'code': '',
           'authcode': '登录了你的会员账号，去浏览器里复制cookies',
           'level_id': '2',
           'is_expire': '0',
           'domain': '',
           '_99_mon': '',
           'Hm_lvt_f3c68d41bda15331608595c98e9c3915': '',
           'Hm_lpvt_f3c68d41bda15331608595c98e9c3915': '',
           # 'undefined': '',
           'stat_isNew': '0',
           'looyu_20001269': '好像没什么用',
           '_ga': '', }

def is_ok(str1):
    if isinstance(str1, str):
        return str1.lower() == "ok" or str1.lower() == "y" or str == ''
    else:
        return False


def is_all(str1):
    if isinstance(str1, str):
        return str1.lower() == "a" or str == ''
    else:
        return False


def is_valid_index(index, length):
    if isinstance(index, int):
        if (index >= 1) and (index <= length):
            return index - 1
    elif isinstance(index, str):
        try:
            index2 = int(index)
        except Exception as e:
            print(e)
            return 0
        else:
            if (index2 >= 1) and (index2 <= length):
                return index2 - 1
    else:
        return 0


def replace_special(source_str):
    special = ('/', '\\', ':', '<', '>', '|', '*', '?', '"', ' ')
    for s in special:
        source_str = source_str.replace(s, "")
    return source_str

if __name__ == '__main__':
    jieguo = is_valid_index("3", 10)
    print(jieguo)
    print(is_ok("Ok"))
    print(is_ok("oo"))
    print("特殊字符替换", replace_special('/ \\ " ? * | < > : '))