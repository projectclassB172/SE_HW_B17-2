#2k = -9                       //变量名不能以数字开头，应该改为 k = -9
# if 2k >=0:                  // python 对于缩进很严格此处if前有一个空格导致程序编译出错，2k应该变为k.修改为if k>=0:
#  with = 2k + "正数"   // with是关键字，不能作为变量名，应改为w=k+"正数"
#   print(with)               //改为print(w)
#  else:                         //python 对于缩进很严格此处else应该和前面的if缩进一致。
#   print(2K+'负数")     //引用字符串不能 ' " 应该使用' '引用或者" "引用，同时python不支持对不同类型变量进行字符串拼接
#                                 //应该将int类型的变量强制转换str类型再进行拼接



修改后的代码

k = -9
if k >=0:
 w=str(k)+"正数"
 print(w)
else:
  print(str(k)+"负数"))