Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

            
公鸡: 0只, 母鸡: 25只, 小鸡: 75只
公鸡: 3只, 母鸡: 20只, 小鸡: 77只
公鸡: 4只, 母鸡: 18只, 小鸡: 78只
公鸡: 7只, 母鸡: 13只, 小鸡: 80只
公鸡: 8只, 母鸡: 11只, 小鸡: 81只
公鸡: 11只, 母鸡: 6只, 小鸡: 83只
公鸡: 12只, 母鸡: 4只, 小鸡: 84只
>>> 
