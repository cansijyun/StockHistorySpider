# -*- coding:utf-8 -*-
"""
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

VERSION = '0.5.1'

CODE_LIST_URL = 'http://quote.eastmoney.com/stocklist.html'
DATE_PARSE_URL = 'http://quotes.money.163.com/trade/lsjysj_%s.html'
# %code
DATA_REQUEST="http://quotes.money.163.com/service/chddata.html?code=0%s&start=%s&end=%s&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
#%(code,start_data,end_data)


