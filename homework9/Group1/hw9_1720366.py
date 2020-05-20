import mysql.connector
import os
import codecs
user='root';
pwd='root';
host='localhost';
db='mysql';
charset='UTF-8'
cnx = mysql.connector.connect(user=user,password=pwd, host=host, database=db)
cursor = cnx.cursor(dictionary=True)
print(insert('gelixi_help_type',{'type_name':'\'sddfdsfs\'','type_sort':'283'}))
def insert(table_name,insert_dict):
param='';
value='';
if(isinstance(insert_dict,dict)):
for key in insert_dict.keys():
param=param+key+","
value=value+insert_dict[key]+','
param=param[:-1]
value=value[:-1]
sql="insert into %s (%s) values(%s)"%(table_name,param,value)
cursor.execute(sql)
id=cursor.lastrowid
cnx.commit()
return id

def delete(table_name,where=''):
if(where!=''):
str='where'
for key_value in where.keys():
value=where[key_value]
str=str+' '+key_value+'='+value+' '+'and'
where=str[:-3]
sql="delete from %s %s"%(table_name,where)
cursor.execute(sql)
cnx.commit()

print(select({'table':'gelixi_help_type','where':{'help_show': '1'}},'type_name,type_id'))
def select(param,fields='*'):
table=param['table']
if('where' in param):
thewhere=param['where']
if(isinstance (thewhere,dict)):
keys=thewhere.keys()
str='where';
for key_value in keys:
value=thewhere[key_value]
str=str+' '+key_value+'='+value+' '+'and'
where=str[:-3]
else:
where=''
sql="select %s from %s %s"%(fields,table,where)
cursor.execute(sql)
result=cursor.fetchall()
return result

table string 表名
return string 建表语句
def showCreateTable(table):
sql='show create table %s'%(table)
cursor.execute(sql)
result=cursor.fetchall()[0]
return result['Create Table']
print(showCreateTable('gelixi_admin'))
def showColumns(table):
sql='show columns from %s '%(table)
print(sql)
cursor.execute(sql)
result=cursor.fetchall()
dict1={}
for info in result:
dict1[info['Field']]=info
return 