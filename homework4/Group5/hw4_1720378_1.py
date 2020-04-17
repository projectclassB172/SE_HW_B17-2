#设公鸡x只，母鸡y只，小鸡z只。
# 因为公鸡最多买20只，母鸡最多买33只。所以0<x<20, 0<y<33, z=100-x-y。
for x in range(0,20):
	for y in range(0,33):
		z=100-x-y
		if 5*x+3*y+z/3 == 100:
			print('公鸡：%s 母鸡：%s 小鸡：%s'%(x, y, z))