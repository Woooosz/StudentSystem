from dao.decorator import db_helper, db_helper_no_json
import pymysql
import json

def mapping(x):
    if x is None:
        return None
    return {'workroom_id':x[0], 'roomname': x[1], 'capacity': x[2], 'support_name': x[3], 'work_organization':x[4], 'used':x[5], 'rate':x[6]}

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
    sql_get = "SELECT * FROM vw_workroom WHERE roomname like '%%%s%%' and support_name like '%%%s%%' and work_organization like '%%%s%%' LIMIT  %d, %d" % (tutor_id, tutor_name, tutor_phone, (int(page) - 1) * int(pageSize), (int(page)) * int(pageSize))
    cursor.execute(sql_get)
    res = cursor.fetchall()
    res2 = []
    for i in res:
        # 这里有问题
        print(i)
        rate = str(round(100* (float(i[5]) / float(i[2])),2)) + '%'
        ls = list(i)
        ls.append(rate)
        res2.append(ls)

    sql_get = "SELECT COUNT(*)  AS cnt FROM vw_workroom WHERE support_name like '%%%s%%' and work_organization like '%%%s%%' " % (tutor_name, tutor_phone)
    cursor.execute(sql_get)
    cnt = cursor.fetchone()[0]
    return res2, cnt

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
