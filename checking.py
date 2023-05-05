import time

st = time.time()

x = [1, 2, 3]
# print(len(x))
for i in range(1000):
    x.append(i)

et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
