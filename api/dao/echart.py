import json
import pymysql
import config


def echart1():
    nianji_list = []
    nianji_data = []
    with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
        conn.execute("select nianji, count(*) as num from student group by nianji")
        results = conn.fetchall()
        for row in results:
            nianji_list.append(row[0])
            nianji_data.append(row[1])
    data = {'xAxis': { 
            'data': nianji_list
        },
        'yAxis': {},
        'series': [{
            'name': '人数',
            'type': 'bar',
            'data': nianji_data
        }]}
    return data

def echart2():
    nianji_list = []
    nianji_data = []
    data_list = []
    with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
        conn.execute("select zhuanye, count(*) as num from student group by zhuanye")
        results = conn.fetchall()
        for row in results:
            nianji_list.append(row[0])
            nianji_data.append(row[1])
            data_list.append({'value':row[1], 'name':row[0]})
    data = {
        'series': [{
                'name':'经济管理学院',
                'type':'pie',
                'radius' : [30, 110],
                'roseType' : 'area',
                'data':data_list}],
        'data':nianji_list
    }
    return data

def echart3():
    res_dict = {}
    zhuanye_set = set()
    nianji_set = set()
    with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
        conn.execute("select nianji, zhuanye, count(*) from student group by nianji, zhuanye")
        results = conn.fetchall()
        for row in results:
            zhuanye_set.add(row[1])
            res_dict[row[1]] = {row[0]:row[2]}
            nianji_set.add(row[0])
    for k,v in res_dict.items():
        for nianji in nianji_set:
            if not nianji in v.keys():
                v[nianji] = 0
        res_dict[k] = sorted(v.items(), key=lambda d:d[0], reverse = True) 
    nianji_list = sorted(list(nianji_set), reverse=True)
    data = {}
    data['series'] = []
    for k,v in res_dict.items():
        sublist = []
        for vv in v:
            sublist.append(vv[1])
        subdata = {
                'name': k,
                'type': 'bar',
                'stack': '人数',
                'label': {
                    'normal': {
                        'show': 'true',
                        'position': 'insideRight'
                    }
                },
                'data': sublist
            }
        data['series'].append(subdata)
    data['nianji'] = nianji_list
    data['zhuanye'] = list(zhuanye_set)
    return data

def echart4():
    workroom_list = ['教研室']
    used_list = ['已使用']
    ununsed_list = ['未使用']
    with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
        conn.execute("select roomname, capacity, used from vw_workroom order by used/capacity desc limit 8")
        results = conn.fetchall()
        for row in results:
            workroom_list.append(row[0])
            used_list.append(int(row[2]))
            ununsed_list.append(int(row[1]) - int(row[2]))
    data = {}
    data['source'] = []
    data['source'].append(workroom_list)
    data['source'].append(used_list)
    data['source'].append(ununsed_list)

    data['series'] = []
    center_list = [['20%', '30%'],['40%', '30%'],['60%', '30%'],['80%', '30%'],
    ['20%', '70%'],['40%', '70%'],['60%', '70%'],['80%', '70%']]
    for idx in range(len(center_list)):
        subdata = {
                'type': 'pie',
                'radius': 70,
                'name':workroom_list[idx+1],
                'center': center_list[idx],
                'encode': {
                    'itemName': '教研室',
                    'value': workroom_list[idx+1]
                }
            }
        data['series'].append(subdata)
    return data

def echart5():
    xueweileixing_list = []
    peiyangfangshi_list = []
    with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
        conn.execute("select xueweileixing, count(*) as num from student group by xueweileixing")
        results = conn.fetchall()
        cnt = 0
        for row in results:
            if cnt != 0:
                xueweileixing_list.append({'value':row[1], 'name':row[0]})
            else:
                xueweileixing_list.append({'value':row[1], 'name':row[0], 'selected':'true'})
                cnt += 1
        
        conn.execute("select peiyangfangshi, count(*) as num from student group by peiyangfangshi")
        results = conn.fetchall()
        for row in results:
            peiyangfangshi_list.append({'value':row[1], 'name':row[0]})

    data = {
        'xueweileixing': xueweileixing_list,
        'peiyangfangshi':peiyangfangshi_list
    }
    return data


def getechart():
    data = {}
    data['chart1'] = echart1()
    data['chart2'] = echart2()
    data['chart3'] = echart3()
    data['chart4'] = echart4()
    data['chart5'] = echart5()
    return data