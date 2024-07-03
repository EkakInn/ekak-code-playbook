import time
start_time=time.time()
for i in range(1000):
    for j in range(100):
            print(i,j)
print(time.time()-start_time)

#avoid print in production
