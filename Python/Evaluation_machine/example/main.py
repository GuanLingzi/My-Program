f = open("black.in")
f_in = f.read().strip()
f.close()

f = open("black.out", "w")
f.write(f_in * 3)
f.close()

f = open("black.out")
f_out = f.read().strip()
f.close()
f = open("black.ans")
f_ans = f.read().strip()
if f_ans == f_out:
    print("AC")
else:
    print("WA")
f.close()
