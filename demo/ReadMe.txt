1. 已通过测试环境为python3.7
2. GetMetro.py 文件获取地铁站所有站名和经纬度信息，x为经度，y为纬度。
	调用方法：导入模块，然后调用模块里包含的函数：get_result(self, decodejson)，会返回一个包含所有地铁信息的列表。
	from GetMetro import *
	info=GetMetro()
	list = info.get_result(info.get_metroinfo())
3. GetEstate.py 文件获取所有小区名和经纬度信息，x为经度，y为纬度。
4. metro.txt是程序自动保存的地铁站信息。
5. estate.txt是程序自动保存的小区信息。
6. TransferUtil.py 文件是用于坐标系转换的工具包