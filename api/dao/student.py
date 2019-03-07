from dao.decorator import db_helper, db_helper_no_json
from dao.studentDataSchemaList import getSchema
import pymysql
import json

def mapping(x):
    if x is None:
        return None
    return {'id':x[0], 'xueweileixing': x[1], 'peiyangfangshi': x[2], 'xuehao': x[3],'xingming':x[4],'nianji':x[5],'zhuanye':x[6],'daoshi':x[7],'daoshidianhua':x[8],'biyeyuanxiao':x[9],'xingbie':x[10],'zhengzhimianmao':x[11],'jiatinglianxiren':x[12],'sos_relation':x[13],'jiatinglianxidianhua':x[14],'jiatingzhuzhi':x[15],'minzu':x[16],'hunfou':x[17],'chushengriqi':str(x[18]),'shenfenzhenghaoma':x[19],'shoujihaoma':x[20],'email':x[21],'shifouzhuxiao':x[22],'xiaowaizhuzhi':x[23],'susheid':x[24],'fangjianhao':x[25],'gongzuoshi':x[27],'gongweihao':x[28],'suozaifuzeren':x[29],'yanjiusuo':x[30]}

def get_schema():
    result = {}
    data, query = getSchema()
    result['data'] = {'querySchema':query, 'dataSchema':data}
    result['status'] = 1
    result['message'] = 'success'
    result['success'] = True
    result['total'] = None
    return result

@db_helper(lambda x: [mapping(y) for y in x])
def get_tutor(xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye, page, pageSize, conn=None):
    cursor = conn
    sql_get = "SELECT * FROM vw_user where stuid like '%%%s%%' and xingming like '%%%s%%' and nianji like '%%%s%%' and shoujihaoma like '%%%s%%' and roomname in (%s) and xueweileixing in (%s) and peiyangfangshi in (%s) and zhengzhimianmao in (%s) and zhuanye in (%s) LIMIT  %d, %d" \
        % (xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye, (int(page) - 1) * int(pageSize), (int(page)) * int(pageSize))
    print(sql_get)
    cursor.execute(sql_get)
    res = cursor.fetchall()

    sql_get = "SELECT count(*) FROM vw_user where stuid like '%%%s%%' and xingming like '%%%s%%' and nianji like '%%%s%%' and shoujihaoma like '%%%s%%' and roomname in (%s) and xueweileixing in (%s) and peiyangfangshi in (%s) and zhengzhimianmao in (%s) and zhuanye in (%s)" \
     % (xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye)
    cursor.execute(sql_get)
    cnt = cursor.fetchone()[0]
    return res, cnt
