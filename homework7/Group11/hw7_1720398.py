#<1> ��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

def num_1(x , y):
    for i in range(1, min(x , y) + 1):
        if (x % i == 0 and y % i == 0):
            gys = i
    gbs = (x * y) // gys
    return(gys , gbs)
print(num_1(6,15))

#2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����
def count(s):
    digit,alpha,space,other = 0,0,0,0
    for i in s:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('���ֵĸ�����{}\t��ĸ�ĸ�����{}\t�ո�ĸ�����{}\t�����ĸ�����{}'.format(digit,alpha,space,other))
count(input("�������ַ�����"))
#���н��:
�������ַ�����asdf   #$%2^5
���ֵĸ�����2	��ĸ�ĸ�����4	�ո�ĸ�����3	�����ĸ�����4
