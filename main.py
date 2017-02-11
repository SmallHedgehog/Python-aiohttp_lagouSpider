# coding: utf-8

import json
import asyncio
import aiohttp
import requests
import constants
import writer

""" Python中的异步IO和协程(Coroutine), 应用在爬虫中 """

# 解析数据
def parse(jsonData):
    jsonObj = json.loads(jsonData)
    listResult = jsonObj['content']['positionResult']['result']
    info_list = []
    for item in listResult:
        info = []
        info.append(item['companyFullName'].strip())
        info.append(item['positionName'].strip())
        info.append(item['salary'].strip())
        info.append(item['city'].strip())
        # print (item['companyFullName'], item['companyShortName'], item['positionName'], item['salary'], item['positionAdvantage'])
        if info is None:
            continue
        info_list.append(info)
    return info_list

# 使用Python3.5中的异步IO http请求库aiohttp
"""
通过关键字async定义协程
"""
async def get(url, page, keyName):
    data = {
        "first": 'true',
        "pn": page,
        "kd": keyName
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=constants.headers) as resp:
            info_list = parse (await resp.text())
            writer.saveCSV(info_list)

def main(keyName):
    # 得到一个事件循环模型
    loop = asyncio.get_event_loop()
    # 初始化任务列表
    tasks = []
    page = 1
    while page < 31:
        tasks.append(get("http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false", page, keyName))
        page = page + 1
    # 执行任务
    loop.run_until_complete(asyncio.wait(tasks))
    # 关闭事件循环列表
    loop.close()
    writer.closeFile()

if __name__ == '__main__':
    main("Python")

