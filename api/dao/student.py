from dao.decorator import db_helper, db_helper_no_json
from dao.studentDataSchemaList import getSchema
import pymysql
import json

def mapping(x):
    if x is None:
        return None
    return {'id':x[0], 'xueweileixing': x[1], 'peiyangfangshi': x[2], 'xuehao': x[3],'xingming':x[4],'nianji':x[5],'zhuanye':x[6],'biyeyuanxiao':x[7],'xingbie':x[8],'zhengzhimianmao':x[9],'jiatinglianxiren':x[10],'sos_relation':x[11],'jiatinglianxidianhua':x[12],'jiatingzhuzhi':x[13],'minzu':x[14],'hunfou':x[15],'chushengriqi':str(x[16]),'shenfenzhenghaoma':x[17],'shoujihaoma':x[18],'email':x[19],'shifouzhuxiao':x[20],'xiaowaizhuzhi':x[21],'susheid':x[22],'fangjianhao':x[23],'gongzuoshi':x[25],'gongweihao':x[26],'daoshibianhao':x[24]}

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
    sql_get = "SELECT * FROM student where stuid like '%%%s%%' and xingming like '%%%s%%' and nianji like '%%%s%%' and shoujihaoma like '%%%s%%' and roomname in (%s) and xueweileixing in (%s) and peiyangfangshi in (%s) and zhengzhimianmao in (%s) and zhuanye in (%s) LIMIT  %d, %d" \
        % (xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye, (int(page) - 1) * int(pageSize), (int(page)) * int(pageSize))
    print(sql_get)
    cursor.execute(sql_get)
    res = cursor.fetchall()

    sql_get = "SELECT count(*) FROM student where stuid like '%%%s%%' and xingming like '%%%s%%' and nianji like '%%%s%%' and shoujihaoma like '%%%s%%' and roomname in (%s) and xueweileixing in (%s) and peiyangfangshi in (%s) and zhengzhimianmao in (%s) and zhuanye in (%s)" \
     % (xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye)
    cursor.execute(sql_get)
    cnt = cursor.fetchone()[0]
    return res, cnt

@db_helper_no_json()
def delete_tutor(tutor_id, conn=None):
    cursor = conn
    converted = tutor_id
    sql_delete = "DELETE FROM student WHERE id IN (%s)" % (converted)
    row = cursor.execute(sql_delete)
    return row, None

@db_helper(mapping)
def add_tutor(xuehao, xingming, nianji, shoujihaoma, gongzuoshi, xueweileixing, peiyangfangshi, zhengzhimianmao, zhuanye, biyeyuanxiao, xingbie, jiatinglianxiren, sos_relation, jiatinglianxidianhua, jiatingzhuzhi, minzu, hunfou, chushengriqi, shenfenzhenghaoma, email, shifouzhuxiao, xiaowaizhuzhi, susheid, fangjianhao, gongweihao, daoshibianhao, conn=None):
    cursor = conn
    sql_insert = "INSERT INTO student VALUES (NULL, '%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (xueweileixing, peiyangfangshi, xuehao, xingming, nianji, zhuanye, biyeyuanxiao, xingbie, zhengzhimianmao, jiatinglianxiren, sos_relation, jiatinglianxidianhua, jiatingzhuzhi, minzu, hunfou,chushengriqi, shenfenzhenghaoma, shoujihaoma, email, shifouzhuxiao, xiaowaizhuzhi, susheid, fangjianhao, daoshibianhao, gongzuoshi, gongweihao)
    cursor.execute(sql_insert)
    return ((cursor.lastrowid, xueweileixing, peiyangfangshi, xuehao, xingming, nianji, zhuanye, biyeyuanxiao, xingbie, zhengzhimianmao, jiatinglianxiren, sos_relation, jiatinglianxidianhua, jiatingzhuzhi, minzu, hunfou,chushengriqi, shenfenzhenghaoma, shoujihaoma, email, shifouzhuxiao, xiaowaizhuzhi, susheid, fangjianhao, daoshibianhao, gongzuoshi, gongweihao)), None


