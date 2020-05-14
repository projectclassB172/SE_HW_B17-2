��Ŀ<1>
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

��Ŀ<2>
week = int(input('����������1-7��'))
dateweek = ['��һ','�ܶ�','����','����','����','����','����']
print(f'{dateweek[num-1]}')

��Ŀ<3>
import re
language = 'Python is the BEST programming Language��'
result = re.search('^[a-z]+$', language)
if result:
    print ('ȫ����Сд' )
else:
    print ('��ȫ��Сд')

��Ŀ<4>
text = input("������һ���ַ�����")
result = re.search(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})',text)
print('�绰�����ǣ� '+ result.group(0))

��Ŀ<5>
day = '������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25'
dateday = re.compile(r'\d{4}-\d{2}-\d{2}')
dateday = dateday.findall(day)
print("".join(dateday))
