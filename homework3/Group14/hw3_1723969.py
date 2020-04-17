'''
2k=-9 //变量名必须以字母或下划线开头,2k可改为k
 if 2k>=0: //同一级别代码，缩进要一致，缩进两格
   with=2k+"正数" //不能使用关键字作变量名，with->w,以及2k->k
                //且k是数字(int类型)与字符串不能直接用“+”连接，k->str(k)
     print(with) //with->w,且同一级别代码，缩进要一致，缩进两格
   else: //if与else同一级别，缩进四格
   print(2k+"负数") //同上2k->str(k)
'''

#修改
k=-9
if k>=0:
    w=str(k)+"正数"
    print(w)
else:
    print(str(k)+'负数')
#运行结果
#-9负数
#Process finished with exit code 0

