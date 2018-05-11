#!/usr/bin/python
# coding=utf-8

### Custom import
import lalala.functions as fn
import lalala.database as mysql
from lalala.functions import debug
from global_var import *

def test_functions():    
    ### Initialize configuration
    status, config = fn.system_init()
    ### Print out setting variables
    if IS_DEBUG:
        debug(status)
        debug(config)
    assert test_mysql() == 200

def test_mysql():
    status, config = fn.system_init()
    if status != 200:
        return
    db_config = config['database']
    conn, message = mysql.connect(db_config['host'], db_config['port'], db_config['database'], db_config['username'], db_config['password'])
    # conn, message = mysql.connect_via_config(db_config)
    if IS_DEBUG:
        debug(conn, message)
    if conn == None:
        return 200
    ### Insert
    sql = "insert into `chinatimes` (`title`, `url_link`, `content`, `root_category`, `category`, `published_date`) values (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%%Y-%%m-%%d'));"
    message, code = mysql.non_query(conn, sql, 'test title', 
        'test url', 'test content', 'test root category', 'test category', '1970-01-30')
    if IS_DEBUG:
        debug(sql, message, code)
    ### Select
    sql = "select * from chinatimes"
    result, message, code = mysql.query(conn, sql)
    if code == 200:
        debug(sql, result)
    ### Delete
    sql = "delete from `chinatimes` where title=%s;"
    message, code = mysql.non_query(conn, sql, 'test title')
    if IS_DEBUG:
        debug(sql, message, code)
    mysql.close(conn)

    return 200

if __name__ == '__main__':
    test_functions()