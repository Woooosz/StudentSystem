#encoding=utf8
from dao.decorator import db_helper, db_helper_no_json
import pymysql
import json

def mapping(x):
    if x is None:
        return None
    return {'id':x[0], 'tutor_id': x[1], 'tutor_name': x[2], 'tutor_phone': x[3]}

def get_schema():
    result = {}
    result['data'] = {'querySchema':[], 'dataSchema':[]}
    result['status'] = 1
    result['message'] = 'success'
    result['success'] = True
    result['total'] = None
    return result

@db_helper(lambda x: [mapping(y) for y in x])
def get_tutor(tutor_id, tutor_name, tutor_phone, page, pageSize, conn=None):
    cursor = conn
    tutor_name = '' if tutor_name is None else tutor_name
    tutor_phone = '' if tutor_phone is None else tutor_phone
    tutor_id = '' if tutor_id is None else tutor_id
    sql_get = "SELECT * FROM tutor WHERE tutor_id like '%%%s%%' and tutor_name like '%%%s%%' and tutor_phone like '%%%s%%' LIMIT  %d, %d" % (tutor_id, tutor_name, tutor_phone, (int(page) - 1) * int(pageSize), (int(page)) * int(pageSize))
    cursor.execute(sql_get)
    res = cursor.fetchall()

    sql_get = "SELECT COUNT(*)  AS cnt FROM tutor WHERE tutor_name like '%%%s%%' and tutor_phone like '%%%s%%' " % (tutor_name, tutor_phone)
    cursor.execute(sql_get)
    cnt = cursor.fetchone()[0]
    return res, cnt

@db_helper(mapping)
def add_tutor(tutor_id, tutor_name, tutor_phone, conn=None):
    cursor = conn
    sql_insert = "INSERT INTO tutor VALUES (NULL, '%s','%s', '%s')" % (tutor_id, tutor_name, tutor_phone)
    cursor.execute(sql_insert)
    return ((cursor.lastrowid, tutor_id, tutor_name, tutor_phone)), None

@db_helper_no_json()
def delete_tutor(tutor_id, conn=None):
    cursor = conn
        # converted = "'"
        # for s in tutor_id:
        #     if s != ',':
        #         converted += s
        #     else:
        #         converted += "','"
        # converted += "'"
    converted = tutor_id
    sql_delete = "DELETE FROM tutor WHERE id IN (%s)" % (converted)
    row = cursor.execute(sql_delete)
    return row, None

@db_helper_no_json()
def update_tutor(id, tutor_id, tutor_name, tutor_phone, conn=None):
    cursor = conn
    sql_update = "UPDATE tutor SET tutor_id = IF(STRCMP('%s', 'None'), '%s',tutor_id), " \
                 "tutor_name=IF(STRCMP('%s', 'None'), '%s',tutor_name), " \
                 "tutor_phone=IF(STRCMP('%s', 'None'), '%s',tutor_phone) " \
                 "WHERE id IN(%s)" % (tutor_id, tutor_id, tutor_name, tutor_name,tutor_phone, tutor_phone, id)
    # UPDATE
    # tutor
    # SET
    # tutor_id = COALESCE(NULL, tutor_id)
    # WHERE
    # id
    # IN(3)
    print(sql_update)
    row = cursor.execute(sql_update)
    return row, None

def upload(f):
    successCnt = 0
    errorCnt = 0
    index = 0
    errorlist = []
    try:
        for line in f:
            s = str(line, encoding = "utf-8")
            lis = s.strip('\r\n').split(',')
            try:
                add_tutor(lis[0], lis[1], lis[2])
                successCnt = successCnt + 1
            except:
                if len(errorlist) == 0:
                    errorlist.append(str(cnt + 1))
                else:
                    errorlist.append(','+str(cnt + 1))
                errorCnt += 1
            index = index + 1
        if errorCnt == 0:
            res = {"data":"导入成功{0}条。".format(successCnt), "message":"","success":True,"total":0}
        else:
            res = {"data":"导入成功{0}条，导入失败{1}条，导入失败的行：{2}".format(successCnt, errorCnt, ''.join(errorlist)), "message":"","success":True,"total":0}
    except:
        res = {"data":"导入失败，请重试。", "message":"","success":False,"total":0}
    return res

def download(q):
    return 'success'