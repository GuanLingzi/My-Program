import sys
import os
import time

sys.stdin = open('test.in')
console = sys.stdout
sys.stdout = open('test.out', 'w')
###############

f = open('test.py')
s = f.read().strip()
t = time.time()

try:
    exec(s)
except:
    sys.stdin.close()
    sys.stdout.close()
    sys.stdout = console
    t1 = time.time() - t
    print('Runtime Error')
else:
    sys.stdin.close()
    sys.stdout.close()
    sys.stdout = console
    t1 = time.time() - t
    with open('test.ans') as f:
        f_ans = f.read().strip()
    with open("test.out") as f:
        f_out = f.read().strip()
    if f_ans == f_out:
        print("All Accepted")
    else:
        print("Wrong Answer")
        os.system('diff -b test.out test.ans')
finally:
    print('used time:', t1 * 1000, "ms.")
###############
