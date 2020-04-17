sum=0
for i in range(20):
    for j in range(33):
        for k in range(100):
            if (5*i+3*j+k==100) and ((i+j+3*k)==100):
                sum+=1
print(sum)