1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(m,n):
    if m>n:
            m,n = n,m
    p = m*n
    while m!=0:
            r = n%m
            n = m
            m = r
    return(n,p//n)
print(demo(12,30))
2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。以及其它的个数。
print('first'.center(40,'='))
def fun1(str1):    
  dig = 0    
  al = 0    
  tb = 0    
  other = 0    
  for i in str1:        
    i = ord(i)        
    if i >= 48 and i <=57:                   dig += 1        
    elif (i >= 65 and i <= 90) or (i >= 97 and i <= 122):            
        al += 1        
    elif i == 32:            
        tb += 1       
    else:            
        other += 1    
print('字符串中【数字】{}个、【字母】{}个、【空格】{}个 、 【其他】{}个'.format(dig,al,tb,other))str2 = input("Please enter the first string:")fun1(str2)  
