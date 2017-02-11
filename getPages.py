# coding: utf-8

import constants
import re
import urllib
import requests

""" 获取到每个职位关键字对应的招聘信息的页数"""

base_url = "https://www.lagou.com/jobs/list_"
base_data = {
    "px": "new",
    "city": "全国"
}

# 编码数据
encodeDatas = []
for item in constants.key_name:
    encodeData = urllib.parse.urlencode({"key": item}).split("=")[-1]
    encodeDatas.append(encodeData)

# 获取到完整的url地址
def get_completeUrls():
    complete_urls = []
    for item in encodeDatas:
        url = base_url + str(item) + "?" + urllib.parse.urlencode(base_data)
        complete_urls.append(url)
    return complete_urls

# 获取到每个职位关键字对应的招聘信息的页数
def get_totalPages(complete_urls):
    if complete_urls is None:
        return None
    else:
        dict_keyNum = {}
        for index in range(len(complete_urls)):
            req = requests.get(complete_urls[index], headers=constants.headers)
            print (req.content)

get_totalPages(get_completeUrls())
            
