conn = sqlite3.connect("test.db")
per_name=input('请输入需要删除的联系人姓名：')
conn.execute("delete from USER where NAME = '%s'" %(per_name))

conn.commit()

print("删除中 :", conn.total_changes)
num1=conn.total_changes
print(f"{num1} rows changed in table USER.")


class Person:
    def __init__(self, NAME, ID,TEL,ADDRESS):
        self.NAME = NAME
        self.ID = ID
        self.TEL = TEL
        self.ADDRESS = ADDRESS
