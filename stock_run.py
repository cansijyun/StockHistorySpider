# coding=utf-8
import requests
import re
from lxml import etree
import time
import stock_vas as sv


def get_stock_list():
   url=sv.CODE_LIST_URL
   response = requests.get(url)
   if response.status_code == 200:
       response = etree.HTML(response.content)
   node_list = response.xpath('//*[@id="quotesearch"]/ul/li')

   code_list = []
   for node in node_list:
       try:
           code = re.match(r'.*?\((\d+)\)', etree.tostring(node).decode()).group(1)
           if code[0]=='0'or code[0]=='6':
               code_list.append(code)
       except:
           continue
   print(code_list)
   return code_list

def download_date(code):
    url=sv.DATE_PARSE_URL%code
    response = requests.get(url)
    if response.status_code == 200:
        response = etree.HTML(response.content)
        start_date = ''.join(response.xpath('//input[@name="date_start_type"]/@value')[0].split('-'))
        end_date = ''.join(response.xpath('//input[@name="date_end_type"]/@value')[0].split('-'))
    return start_date,end_date

def download_history_data(code,path='data/'):
    date_list=download_date(code)
    start_data=date_list[0]
    end_date=date_list[1]
    download_url=sv.DATA_REQUEST%(code,start_data,end_date)

    data = requests.get(download_url)
    with open(path+code+'.csv', 'wb') as f:
        #一般情况下，应该以下面的模式将文本流保存到文件：
        for chunk in data.iter_content(chunk_size=10000):
            if chunk:
                f.write(chunk)
    print('股票---',code, '历史数据正在下载')

def download_all_hitory(exchange='all',path=''):
    if exchange == 'all':
        code_list = get_stock_list()
    if exchange == 'sz':
        code_list = ''
    if exchange == 'sh':
        code_list = ''

    for temp_code in code_list:
        time.sleep(1)
        download = download_history_data(temp_code,path)
        download.run()

'''
download_history_data('000002')
download_history_data('000002','D:/temp/data')
'''

'''
list=get_stock_list() #获得全部股票
download_history_data('000002') #获得000002数据
'''

