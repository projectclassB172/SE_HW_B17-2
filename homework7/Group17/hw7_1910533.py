1.
def ly(m,n):
     if m>n:
             m,n = n,m
     p = m*n
     while m!=0:
             r = n%m
             n = m
             m = r
     return(n,p//n)

print(ly(12,30))

2.
def count(n):
  alpha,num,space,other=0,0,0,0
  for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        space+=1
    else:
         other+=1
  print('英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(alpha,num,space,other))
count(input("请输入一个字符串："))