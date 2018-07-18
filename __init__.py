__version__ = '0.8.6'
__author__ = 'Jimmy Liu'
"""
for trading data
"""
from stock_run import (download_date,download_all_hitory)

'''
download_history_data('000002')
download_history_data('000002','D:/temp/data')
'''

'''
list=get_stock_list() #获得全部股票
download_all_hitory('sz') #获得全部深圳股票
download_history_data('000002') #获得000002数据
'''
