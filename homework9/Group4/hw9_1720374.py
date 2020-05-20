#1720374�Ƶ���

import sqlite3

class DB:
    
    def create_table(self):
        try:
            cr.execute('''CREATE TABLE t_adb
                (id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL ,
                company TEXT,
                address TEXT);''')
            conn.commit()
            print("t_adb �����ɹ�!\n")
        except sqlite3.OperationalError as reason:
            print("����: t_adb ����ʧ�ܣ� " + str(reason) + "\n")


def addperson(hcon,c):

    id = int(input('���������ID: '))
    name = str(input('�������������: '))
    number = str(input('����������ֻ���: '))
    company = str(input('��������Ĺ�˾: '))
    addr = str(input('��������ĵ�ַ: '))
    sql="insert into person(id,name,number,company,addr) values(?,?,?,?,?)"
    c.execute(sql, (id,name,number,company,addr))
    hcon.commit()
    print("���ֳɹ�")
    hcon.rollback()



def delete(hcon,c):
	selectmail(hcon,c)
	did=int(input('��������Ҫɾ����id�� '))
	sql="delete from person where id=?"
	c.execute(sql,(did,))
	hcon.commit()


def choice():
    print("�����ϵ��������:1")
    print("��ѯ��ϵ��������:2")
    print("ɾ����ϵ��������:3")
    print("�˳��밴4")
    Button = 6
    while (Button>5 or Button<0 ):
        Button = int(input("������:"))
    return Button

def main():
    if os.path.exists('phonenumber.db') == False:
        conphonenumber()
    hcon = sqlite3.connect('phonenumber.db')
    c = hcon.cursor()
    while (True):
        Button = choice()
        if (Button == 1):
            addperson(hcon,c)
        elif(Button == 2):
            selectmail(hcon,c)
        elif(Button == 3):
            delete(hcon, c)
        else:
            break
        print("����")


    c.close()
    hcon.close()

if __name__=="__main__":
	main()