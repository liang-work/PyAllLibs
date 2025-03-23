"""
		  ◢＼　 ☆　　 ／◣
	　  　∕　　﹨　╰╮∕　　﹨
	　  　▏　　～～′′～～ 　｜
	　　  ﹨／　　　　　　 　＼∕
	　 　 ∕ 　　●　　　 ●　 ＼
	  ＝＝　○  ∴  ╰╯　∴　○　＝＝
	　     ╭──╮　　　　　╭──╮
"""
#@name: Python多用途库/Py_All_Libs  #
#@author: Liang_work              #
#@time: 2025年3月8日               #
#@version: 0.1                    #
#=================================#
#使用的三方库/Use Libs              #
"""
MIT wmi, syst(SystemInfo), toml, colorlog
BSD cachelib, psutil
"""

from . import dns,log
from . import SaveFile,LoadFile,syst,nw_socket,SC,hash

dns_record = dns.query_dns_record
whois = dns.whois_query
loger = log.loging

__version__ = "0.1.0"