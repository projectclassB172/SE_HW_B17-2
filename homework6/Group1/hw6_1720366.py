<1>
best_language = 'PHP is the best programming language in the world!'
t1=best_language('PHP','Python')
print(t1)
<2>
num =int(input('请输入1-7之间的数字：'))
if num == 1:    
print('今天是周一')
elif num == 2:    
print('今天是周二')
elif num == 3:    
print('今天是周三')
elif num == 4:    
print('今天是周四')
elif num == 5:    
print('今天是周五')
elif num == 6 or num == 7:    
print('今天是周末')
<3>
char = input("Python is the BEST programming Language！")
lenght = len(char)
j = 0     
a = 0  
while j <= lenght :
    for i in char :
        num = ord(i)  
        if num >= 48 and num <= 57 or num >= 97 and num <= 122 :
            a += 1     
        j += 1
if a == j :     
    print("该字符串由小写字母和数字组成")
else:
    print("该字符串包含大写字母或者是符号！")
<4>
s = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s)
for each in result:
    print(each[0], each[1], each[2], sep="-")
<5>
    function checkDate(value){
        var reg = "^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|          (?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$";
        var regExp = new RegExp(reg);
        if(!regExp.test(value)){
            return false;    
        }else{
            return true;
        }
    }