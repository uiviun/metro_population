#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
# 导入模块
import TransferUtil
 

class Metro:
	def __init__(self,linename,name,x,y):
		self.linename = linename
		self.name = name
		self.x = x
		self.y = y

class GetMetro:
	def __init__(self):
		print ("init")
        
	def get_metroinfo(self):
		return self.__get_metroinfo__()
		
	##用来获取返回的数据
	def __get_metroinfo__(self):
		headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		}
		url='http://map.baidu.com'
		params={
			'qt':'bsi',
			'c':'131',
			't':'123457788'
		}
		response=requests.get(url=url,params=params,headers=headers)
		html=response.text
		print (html)
		decodejson=json.loads(html)
		print(decodejson)
		#print(json.dumps(decodejson, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
		return decodejson
		
	##用来解析处理返回的数据
	def get_result(self, decodejson):
		decodejson = decodejson['content']
		#print(decodejson)
		#用来存储最后地铁结果的列表
		list_value = []
		#遍历所有地铁线路
		for key in decodejson:
			list_key = []
			list = []
			print('----'+str(key['line_name'])+'----')
			list = key['stops']
			#print('----'+str(decodejson)+'----')
			#遍历各个线路的所有地铁站
			for k in range(len(list)):
				#去掉无用信息
				del list[k]['is_practical']
				del list[k]['uid']
				#将墨卡托坐标转换为经纬度坐标
				list[k]['x'] = TransferUtil.ll(list[k]['x'],list[k]['y'])[0]
				list[k]['y'] = TransferUtil.ll(list[k]['x'],list[k]['y'])[1]
				print('----'+str(list[k])+'----')
				#将站名与经纬度信息添加到最后列表中
				list_value.append(list[k])
		return list_value

				
info=GetMetro()
list = info.get_result(info.get_metroinfo())
# 打开一个文件
fo = open("metro.txt", "w+")
# 将结果写入同级目录的文本中
fo.write(str(list))
 
# 关闭打开的文件
fo.close()
