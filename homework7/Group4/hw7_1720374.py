#1720374�Ƶ���
# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������
def getnum(m,n):
    if m>n:
        m,n = n,m
    p = m*n
    while m!=0:
        r = n%m
        n=m
        m=r
    return (n,int(p/n))
print(getnum(20,30))
# ���н����(10, 60)

#2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����
def xx(str1):
    num_number = char_number = space_number = other_number = 0
    for char in str1:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1

    print("���ָ�����%d,��ĸ������%d,�ո������%d,�����ַ���%d" % (num_number, char_number, space_number, other_number))
    return
xx("30jka  96$%  ^&*ss  a555")
#"G:\PyCharm 2019.3.4\venv\Scripts\python.exe" "G:/PyCharm 2019.3.4/hw7_1720374.py"
#���ָ�����7,��ĸ������6,�ո������6,�����ַ���5

#Process finished with exit code 0

