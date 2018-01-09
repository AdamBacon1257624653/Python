import os
import time

g_num = 10
pid = os.fork()
if pid == 0:
    g_num += 1
    print("==================g_num====================%d" % g_num)
else:
    time.sleep(3)
    print("****************g_num******************%d" % g_num)
