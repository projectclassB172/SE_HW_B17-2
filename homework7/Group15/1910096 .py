'''
#1.编写函数，接收两个正整数作为参数，返回一个元组，
其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''
def gongyueshu(i,j):
     if i>j:
            i,j = j,i
     p = j*i
    
     for num in range(1,i):
          if (i%num==0)&(j%num==0):
                         k=num
                         #最大公约数



     
     for l in range(j,p+1):
          if(l%j==0)&(l%i==0):
               m=l#最小公倍数
               break

          
     list1=[k,m]
     print(list1)
     return(tuple(list1))
        
     
    
print(gongyueshu(9,82))
'''
2.编写函数，接受一个字符串作为参数，
计算并打印传入字符串中数字，
字母，空格，以及其它的个数。以及其它的个数。
'''

def fun1(str1):    
  shuzi = 0    
  zimu = 0    
  space = 0    
  other = 0    
  for i in str1:        
    i = ord(i)        
    if i >= 48 and i <=57:
        shuzi += 1        
    elif (i >= 65 and i <= 90) or (i >= 97 and i <= 122):            
        zimu += 1        
    elif i == 32:            
        space += 1       
    else:            
        other += 1    
  print('字符串中数字{}个、字母{}个、空格{}个 、 其他字符{}个'.format(shuzi,zimu,space,other))
str2 = input("请输入验证字符:")
fun1(str2) 

