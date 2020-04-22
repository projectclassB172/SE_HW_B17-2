import re

print(1)
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))

print(2)
weeks = ["一", "二", "三", "四", "五", "六", "七"]
data = int(input("请输入1-7："))
print("今天是周" + weeks[data - 1])

print(3)
if re.match('[a-z]+', "adkkdk"):
    print('全为小写')
else:
    print("不全是小写")

print(4)
a = "afas(139)419-4541gasa"
print(re.search('[1-9]{3}\-[1-9]{3}\-[1-9]{4}|\([1-9]{3}\)[1-9]{3}\-[1-9]{4}', a))

print(5)
a = input()
print(re.search(
    '([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))',
    a))
