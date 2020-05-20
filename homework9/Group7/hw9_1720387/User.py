# User类包括属性：1、姓名 2、电话 3、公司 4、地址
class User():
    def __init__(self ,Name ,Phone ,Company ,Address):
        self._ID = 0
        self._Name = Name
        self._Phone = Phone
        self._Company = Company
        self._Address = Address

    def setID(self,ID):
        self._ID = ID

    def getName(self):
        return self._Name
    def getPhone(self):
        return self._Phone
    def getCompany(self):
        return self._Company
    def getAddress(self):
        return self._Address

    def __str__(self):
        return 'ID:{}\t姓名:{}\t电话:{}\t公司:{}\t地址:{}'.format(self._ID,self._Name,self._Phone,self._Company,self._Address)


