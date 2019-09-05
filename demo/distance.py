#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

def get_distance_bd09(a,b,c,d):
    """
    算法来源：http://developer.baidu.com/map/jsdemo.htm#a6_1
    :param pointA: {lat:29.490295, lng:106.486654}
    :param pointB: {lat:29.615467, lng:106.581515}
    :return:米
    """
    Radius = 6370996.81  # 球半径

    if (a and c):
        if a == c and b == d:
            distance = 0
        else:
            a_lat = a * math.pi / 180
            a_lng = b * math.pi / 180
            b_lat = c * math.pi / 180
            b_lng = d * math.pi / 180
            # print(a_lng,b_lng,a_lat,b_lat)
            distance = Radius * math.acos(
                math.sin(a_lat) * math.sin(b_lat) + math.cos(a_lat) * math.cos(b_lat) * math.cos(b_lng - a_lng))
        return distance
if __name__ == '__main__':
    print(get_distance_bd09(117.267856,39.161639,117.26091141018294,39.0511679181914))