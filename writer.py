# coding: utf-8

import csv

csvFile = open("Python职位信息.csv", 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow([
    "公司名称",
    "招聘职位名称",
    "Salary",
    "地址"
])

def saveCSV(info_list):
    csvWriter.writerows(info_list)

def closeFile():
    csvFile.close()
