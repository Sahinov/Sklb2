#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
mos = sites['Moscow']
lon = sites['London']
par = sites['Paris']

mos_lon = ((mos[0]-lon[0])**2 + (mos[1]-lon[1])**2)**0.5
mos_par = ((mos[0]-par[0])**2 + (mos[1]-par[1])**2)**0.5
lon_par = ((lon[0]-par[0])**2 + (lon[1]-par[1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = mos_lon
distances['Moscow']['Paris'] = mos_par

distances['London'] = {}
distances['London']['Moscow'] = mos_lon
distances['London']['Paris'] = lon_par

distances['Paris'] = {}
distances['Paris']['London'] = lon_par
distances['Paris']['Moscow'] = mos_par

#distances = {'Distance from Moscow to London ': mos_lon,
 #            'Distance from Moscow to Paris ': mos_par,
  #           'Distance from Paris to London ': lon_par}
pprint(distances)





