#encoding=utf8

"""
create db file.
"""

import sqlite3
import os

db_file = 'contact.db'
if os.path.exists(db_file) == False:
    con = sqlite3.connect(db_file) 
    cursor  = con.cursor()
    # 创建表
    sql = '''
    create table contact (
        id int primary key, 
        name varchar(32), 
        mobile char(11), 
        company varchar(128), 
        address varchar(128)
    )
    '''
    cursor.execute(sql)
    cursor.close()
    con.close()
    print("成功创建")
