#设公鸡i只，母鸡z只，小鸡k只。
# 因为公鸡最多买20只，母鸡最多买33只。所以0<x<20, 0<z<33, k=100-x-y。
for i in range(0,20):
	for z in range(0,33):
		k=100-i-z
		if 5*i+3*z+k/3 == 100:
			print('公鸡：%s 母鸡：%s 小鸡：%s'%(i, z, k))