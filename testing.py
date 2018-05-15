#!/usr/bin/python
# coding=utf-8

### Custom import
from lalala.functions import debug, read_config, system_init
from lalala.browser import *
import lalala.database as mysql
from global_var import *

def main():
    status, config = system_init()
    if status != 200:
        return        
    # assert test_mysql() == 200
    assert test_browser() == 200

def test_mysql():
    status, config = system_init()
    if status != 200:
        return 404
    db_config = config['database']
    conn, message = mysql.connect(db_config['host'], db_config['port'], db_config['database'], db_config['username'], db_config['password'])
    if IS_DEBUG:
        debug(conn, message)
    if conn == None:
        return 200
    ### Insert
    sql = "insert into `chinatimes` (`title`, `url_link`, `content`, `root_category`, `category`, `published_date`) values (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%%Y/%%m/%%d'));"
    message, code = mysql.non_query(conn, sql, 'test title 參戰499之亂！洗衣業者推499洗到飽服務', 
        'test url', 'test content', 'test root category', 'test category', '1970/01/30')
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
    ## Close connection
    mysql.close(conn)

    return 200

def test_extract_news(url, root_category, db_config):
    conn, message = mysql.connect_via_config(db_config)
    home_page = open_link(url)
    news = parsing_html(home_page)
    for n in news:
        debug(n.url)
        debug(n.published_date)

    return 200

def test_browser():
    status, config = system_init()
    if status != 200:
        return 404
    urls_chinatimes = config['urls']['chinatimes']
    n_browse = 1

    ### Testing arbitrary link
    # home_page = open_link('https://edition.cnn.com/regions')
    # links = parsing_links(home_page)
    # for link in links:
    #     debug(link.string)

    ### Testing Chinatimes
    for i in range(1, n_browse+1):
        url_life = urls_chinatimes['life'] % i
        url_health = urls_chinatimes['health'] % i
        debug(url_life, url_health)
        ### Lifestyle news
        status = test_extract_news(url_life, 'life', config['database'])

        if status != 200:
            return 404

    return 200

if __name__ == '__main__':
    main()