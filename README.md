股票信息爬虫

股票数据下载应用应用。个股K线历史每天（自从开盘日起），高开低收，成交量等各种数据

命令行pip install tuStockSpider 下载项目到

之后在tuStockSpidert的路径下，如下

/lib/python3/site-packages/tuStockSpider


使用

在编辑器中

import tuStockSpider as tss

tss.download_history_data('000002','D:/temp/data/') #下载000002数据到D:/temp/data/文件夹

tss.download_history_data('000002')  #下载000002数据到默认的/lib/python3/site-packages/tuStockSpider/data文件夹


#慎用download_all_hitor，速度慢而且多次请求

tss.download_all_hitory('') #下载全部股票数据

tss.download_all_hitory('sz') #下载全部深圳证券交易所股票数据

tss.download_all_hitory('sh','shdata/') #下载全部上海证券交易所股票数据到shdata文件夹

