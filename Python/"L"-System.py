import turtle as t

ANGLE = 60
LENGTH = 1.5
TITLE = "CARPET"
AXIOM = "R"
RULES = {"L": "R+L+R", "R": "L-R-L"}
# +:right, -:left, L/R:forward
ITER = 8


def create_l_system(i):
    for a in range(ITER):
        res = ''
        for c in i:
            if c in RULES:
                res += RULES[c]
            else:
                res += c
        i = res
    return res


def draw_l_system(i):
    for c in i:
        if c == 'L':
            t.forward(LENGTH)
        elif c == 'R':
            t.forward(LENGTH)
        elif c == '+':
            t.right(ANGLE)
        elif c == '-':
            t.left(ANGLE)
        else:
            print("Something wrong in your entered command.")
            return


t.tracer(0, 0)
t.hideturtle()

t.up()
t.goto(-(280 / 2), (280 / 2) / 3 ** 0.5)
t.down()

draw_l_system(create_l_system(AXIOM))

t.done()
