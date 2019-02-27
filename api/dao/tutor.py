from dao.decorator import db_helper
import pymysql
import json

def mapping(x):
    if x is None:
        return None
    return {'tutor_id': x[0], 'tutor_name': x[1], 'tutor_phone': x[2]}

def get_schema():
    result = {}
    result['data'] = {'querySchema':[], 'dataSchema':[]}
    result['status'] = 1
    result['message'] = 'success'
    result['success'] = True
    result['total'] = None
    return result

@db_helper(lambda x: [mapping(y) for y in x])
def get_tutor(tutor_name, tutor_phone, page, pageSize, conn=None):
    cursor = conn
    tutor_name = '' if tutor_name is None else tutor_name
    tutor_phone = '' if tutor_phone is None else tutor_phone
    sql_get = "SELECT * FROM tutor WHERE tutor_name like '%%%s%%' and tutor_phone like '%%%s%%' LIMIT  %d, %d" % (tutor_name, tutor_phone, (int(page) - 1) * int(pageSize), (int(page)) * int(pageSize))
    cursor.execute(sql_get)
    res = cursor.fetchall()

    sql_get = "SELECT COUNT(*)  AS cnt FROM tutor WHERE tutor_name like '%%%s%%' and tutor_phone like '%%%s%%' " % (tutor_name, tutor_phone)
    cursor.execute(sql_get)
    cnt = cursor.fetchone()[0]
    return res, cnt

@db_helper(mapping)
def add_tutor(tutor_id, tutor_name, tutor_phone, conn=None):
    cursor = conn
    sql_insert = "INSERT INTO tutor VALUES ('%s','%s', '%s')" % (tutor_id, tutor_name, tutor_phone)
    cursor.execute(sql_insert)
    return ((tutor_id, tutor_name, tutor_phone)), None

@db_helper(mapping)
def delete_tutor(tutor_id, conn=None):
    cursor = conn
    sql_delete = "DELETE FROM tutor WHERE tutor_id = '%s'" % (tutor_id)
    cursor.execute(sql_delete)
    data = cursor.fetchone()[0]
    print(data)