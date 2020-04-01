#假设鸡x只,兔子y只,鸡 兔子共30只.

for x in range(0,30):
    for y in range(0,30):
        if 2*x + 4*y == 90 and x + y == 30:
             print('鸡: %s 兔子: %s'%(x,y))