import sqlite3
conn = sqlite3.connect('addr.db')
print("Opened database successfully")
cursor = conn.cursor()
#�������ݿ��
    try:
        sql='''create table USER (id int primary key, name varchar(20), number char(11), company char(20), addr char(20))'''
        con.execute(sql)
        print("USER �����ɹ�!\n")
    except sqlite3.OperationalError as reason:
        print("����: ����ʧ�ܣ� " + str(reason) + "\n")

# cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
# last_id = cursor.fetchone()
# print(last_id[0])

try:
    _name,_phone,_company,_addr = input("�����������������绰����˾����ַ��ʹ�ÿո������").split()
except:
    print("����,��������\n")
else:
    try:
        cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
        last_id = cursor.fetchone()
        new_id = last_id[0]+1
        cursor.execute('''INSERT INTO user (id,name,number,company,addr) VALUES (?,?,?,?,?)''',(new_id,_name,_number,_company,_addr,))
        conn.commit()
        num1=conn.total_changes
        print("{0} rows changed in table addr.".format(num1))
    except:
        print("��������ظ�����\n")

def select (con,cur):
      try:
        name = input("������Ҫ��ѯ���˵�����:")
        cur.execute("SELECT * From user WHERE  name='{}'".format(name))
        print("��ѯ���Ϊ:{}".fomat.cur.fetchall())
    except:
        print("��������,������ѯ\n")

 def delete(self, name):
        try:
            self.c.execute("DELETE FROM list WHERE name='%s'" % (name))
            self.conn.commit()
            print("ɾ���ɹ���")
        except:
            print("���ȴ������ݿ��!")


cursor.execute("SELECT id,name,company,address From user")
users = cursor.fetchall()
print("��ӡȫ�����ݣ�\n")
print(users)
cursor.close()
conn.close()

if __name__ == "__main__":
    connect = ConnDB()
    connect.close()
