import json
def getechart():
    data = { 'chart1':{'xAxis': { 
            'data': ["2014级", "2015级", "2016级", "2017级", "2018级", "2019级"]
        },
        'yAxis': {},
        'series': [{
            'name': '销量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        }]}}
    return data