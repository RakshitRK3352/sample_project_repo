import time

tic = time.time()
time.sleep(7)
toc = time.time()
print("-----")
print("time taken is---->",toc-tic," sec")
time_diff = toc - tic
time_diff_hrs = time_diff/3600
print("time difference in hours--",time_diff_hrs)
time_diff_mins = time_diff/60
print("time taken in minutes----",time_diff_mins)
