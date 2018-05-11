#!/usr/bin/env python
### Opening mysql through python
"""
Reference for error code
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
"""
import pymysql
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from global_var import *

##### MySQL Connection #####
def connect_via_config(db_config):
    return connect(db_config['host'], db_config['port'], db_config['database'], db_config['username'], db_config['password'])   

def connect(host, port, db, user, passwd):
    messages = []
    if IS_DEBUG:
        messages.append('Trying to connect to {}  (user: {})'.format(host, user))
    conn = None
    try:
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8', autocommit=True)
    except Exception as ex:
        if IS_DEBUG:
            messages.append(str(ex))
        if conn is not None:
            close(conn)
        return None, messages
    if IS_DEBUG:
        messages.append('Connection to {} has been established (user: {})'.format(host, user))
    return conn, messages

def close(conn):
    try:
        conn.close()
        return 'OK'
    except Exception as ex:
        return str(ex)

def query(conn, sql, *args):
    if conn is None:
        return None, "No connection to the mysql server"
    result = []
    message = 'OK'
    cur = conn.cursor()
    param = tuple(arg for arg in args)
    try:
        cur.execute("set names utf8;")
        cur.execute(sql, param)
        for row in cur:
            result.append(row)
    except Exception as ex:
        message = 'Exception in mysql.query : ' + str(ex) + ' (provided sql query was: [' + sql + ']'
        return None, message, 400
    cur.close()
    return result, message, 200

def non_query(conn, sql, *args):
    if conn is None:
        return "No connection to the mysql server", 503
    param = tuple(arg for arg in args)
    message = 'OK'
    cur = conn.cursor()
    try:
        cur.execute("set names utf8;")
        cur.execute(sql, param)
        conn.commit()
    except Exception as ex:
        message = 'Exception in mysql.non_query : ' + str(ex) + ' (provided sql query was: [' + sql + '])'
        return message, 400
    cur.close()
    return message, 200