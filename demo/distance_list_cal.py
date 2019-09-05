#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 导入模块
import distance
import sys
#input_file1=sys.argv[1]
#input_file2=sys.argv[2]
import re

input_file1="./metro_position_input.txt"
input_file2="./estate_position_input.txt"

file = open(input_file1)
lon_station={}
line = file.readline()
line = file.readline()
while line:
    line = line.strip('\n')
    line = line.strip('\r')
    line2 = re.split('\t',line)
    p=len(line2)
    if(p>=3):
        if(re.match('.',line2[2])):
            line2 = line.strip().split('\t')
            #print(line2)
            num1 = float(line2[1])
            lon_station[line2[0]]= line2[1]+"\t"+line2[2]
    line = file.readline()


# 打开一个文件

file2 = open(input_file2)

fo = open("metro_station_estate_distance_cal.txt", "w+")
fo.write('xiaoqv\thushu\t')
for key in lon_station:
    fo.write(key)
    fo.write('\t')
fo.write('\n')
line = file2.readline()
line = file2.readline()
while line:
    line = line.strip('\n')
    line = line.strip('\r')
    line2 = re.split('\t',line)
    if(re.match('.',line2[1])):
        fo.write(line2[0])
        fo.write('\t')
        fo.write(line2[1])
        fo.write('\t')
        for key in lon_station:
            line3 = re.split('\s+',lon_station[key])
            line3[0]=line3[0].strip('\r')
           # print(line2[2],line2[3],line3[0],line3[1])
            line2[2] = float(line2[2])
            line2[3] = float(line2[3])
           # print(line3[0])
            line3[0] = float(line3[0])
            line3[1] = float(line3[1])
            temp=distance.get_distance_bd09(line2[2],line2[3],line3[0],line3[1])
            fo.write(str(temp))
            fo.write('\t')
        fo.write('\n')
    line = file2.readline()
fo.close()


#print(lon_station)

