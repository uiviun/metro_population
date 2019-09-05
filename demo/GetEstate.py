#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import time

#loc_1和loc_2是天津市行政区左下坐标和右上坐标
loc_1 =[38.566667,116.716666]
loc_2 = [40.25,118.066667]
#步长根据测试选择相对合适的值
step = 0.03
#for循环嵌套，获取loc_2与loc_1间步长0.03的矩形区域列表
loc_fin = []
for a in range(1,int((loc_2[0]-loc_1[0])/step+1)+1):
	for b in range(1,int((loc_2[1]-loc_1[1])/step+1)+1):
		lat_1 = round((loc_1[0]+step*a),6)
		lon_1 = round((loc_1[1]+step*b),6)
		lat_2 = round((lat_1-step),6)
		lon_2 = round((lon_1-step),6)
		loc_fin.append(str(lat_2)+","+str(lon_2)+','+str(lat_1)+','+str(lon_1))
#print(loc_fin)
#for循环遍历loc_2与loc_1的矩形区域列表
for loc in loc_fin:
	url = 'http://api.map.baidu.com/place/v2/search?'
	params = {
		'query':'小区',# 此处可以替换为需要查询的内容，如：公交车站$地铁站	地铁站	路
		'bounds':loc,
		'output':'json',
		'page_size':'20',
		'ak':'X52KMvrkBpbKtyu7qCCdXDfWWK8tilwK'
		}
	http_page = requests.get(url,params)
	result = http_page.json()
	#print(result)#查看百度每次返回的结果
	time.sleep(0.025)#受百度并发量限制，上限50次/秒，所以每次查询完sleep0.025秒
	total = result['total']
	#剔除空值，total值大于400输出调小step
	if total > 0 and total < 400:
		result_list = result['results']
		for a in result_list:
			name = a['name']
			lat = a['location']['lat']
			lng = a['location']['lng']
			info = name+','+str(lat)+','+str(lng)+'\n'
			if a['city']=="天津市":#过滤掉天津市以外的信息
				with open('estate_pos.txt','a') as f:
					f.write(info)
				print(info)
	elif total != 0 and total >400:
		with open('estate_pos.txt','a') as f:
			f.write('Please decrease the value of step!'+'\n')
			
f.close()