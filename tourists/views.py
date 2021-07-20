from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
import sys
sys.path.insert(0, 'tourists/resources')
from data import database_update

import json
from threading import Timer

context = {} # "width: 60%"
citymap = {
        'area1': {
            "name" : '꽃사슴 정원',
            "center": { "lat": 37.392476, "lng": 126.639928 },
            "population": 0,
            "desc" : '여유'
        },
        'area2': {
            "name" : '중앙 다리',
            "center": { "lat": 37.39258, "lng": 126.63848 },
            "population": 0,
            "desc" : '여유'
        },
        'area3': {
            "name" : '잔디 광장',
            "center": { "lat": 37.394135, "lng": 126.638070 },
            "population": 0,
            "desc" : '여유'
        },
        'area4': {
            "name" : '테라스 정원',
            "center": { "lat": 37.390063, "lng": 126.640868 },
            "population": 0,
            "desc" : '여유'
        },
        'area5': {
            "name" : '이스트 보트하우스',
            "center": { "lat": 37.390274, "lng": 126.643637 },
            "population": 0,
            "desc" : '여유'
        },
}
def records_update():
    records = database_update()

    for k,n in records[0].items():
        
        if 'id' in k:
            continue

        elif 'time' in k:
            continue
        
        else :
            desc = '여유'
            context[(k+'_num')] = n
            if n >= 80 :
                context[k] = '혼잡'
                desc = '혼잡'
            elif 30<= n < 80:
                context[k] = '보통'
                desc = '보통'
            else:
                context[k] = '여유'

            if k in citymap.keys():
                citymap[k]['population'] = n 
                citymap[k]['desc'] = desc
    print(context)

    Timer(300, records_update).start()

records_update()

# citymap = {
#     'area1': {
#         "name" : '꽃사슴 정원',
#         "center": { "lat": 37.392476, "lng": 126.639928 },
#         "population": 0,
#         "desc" : '여유'
#     },
#     'area2': {
#         "name" : '중앙 다리',
#         "center": { "lat": 37.39258, "lng": 126.63848 },
#         "population": 0,
#         "desc" : '여유'
#     },
#     'area3': {
#         "name" : '잔디 광장',
#         "center": { "lat": 37.394135, "lng": 126.638070 },
#         "population": 0,
#         "desc" : '여유'
#     },
#     'area4': {
#         "name" : '테라스 정원',
#         "center": { "lat": 37.390063, "lng": 126.640868 },
#         "population": 0,
#         "desc" : '여유'
#     },
#     'area5': {
#         "name" : '이스트 보트하우스',
#         "center": { "lat": 37.390274, "lng": 126.643637 },
#         "population": 0,
#         "desc" : '여유'
#     },
# }
# records[0]
# print(records[0])
# context = {} # "width: 60%"
# for k,n in records[0].items():
    
#     if 'id' in k:
#         continue

#     elif 'time' in k:
#         continue
    
#     else :
#         desc = '여유'
#         context[(k+'_num')] = n
#         if n >= 80 :
#             context[k] = '혼잡'
#             desc = '혼잡'
#         elif 30<= n < 80:
#             context[k] = '보통'
#             desc = '보통'
#         if k in citymap.keys():
#             citymap[k]['population'] = n 
#             citymap[k]['desc'] = desc

# print(context)




# Create your views here.
def index(request):
    today = timezone.now().strftime(" %Y 년 %m 월 %d 일 %I:%M:%S%p")
    context['today']= today
    # context['locations']= json.dumps(locations)
    context['citymapJson']= json.dumps(citymap)
    
    return render(request, 'index.html', context=context) 

def button(request):
    context  = { }
    return render(request, 'buttons.html', context)

