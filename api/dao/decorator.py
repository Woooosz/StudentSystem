# decorator.py
import pymysql
import json
import config

def db_helper(jsonfy_rule):
    def wrapper(func):
        def inner(*args, **kwargs):
            with pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,user=config.MYSQL_USRT, password=config.MYSQL_PASSWD, db=config.MYSQL_DB) as conn:
                try:
                    result = func(conn=conn, *args, **kwargs)
                    total = len(result)
                    response = __common_struct(jsonfy_rule(result), total)
                except Exception as e:
                    response = __common_struct(None, None,False, str(e))
            return response
        return inner
    return wrapper


def __common_struct(data, total=None, success=True, error_msg='error'):
    if success:
        result = {}
        result['data'] = data
        result['status'] = 1
        result['message'] = 'success'
        result['success'] = True
        result['total'] = total
        return result
    else:
        result = {}
        result['data'] = data
        result['status'] = 0
        result['message'] = error_msg
        result['success'] = False
        result['total'] = total
        return result
    return result