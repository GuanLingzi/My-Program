import turtle as t

AXIOM = "F--F--F"
RULES = ["F", "F+F--F+F"]
ITER = 4


def create_l_system(i):
    for n in range(ITER):
        i = i.replace(RULES[0], RULES[1])
    return i


def draw_l_system(inst):
    for i in inst:
        if i == 'F':
            t.forward(2)
        elif i == '+':
            t.left(60)
        elif i == '-':
            t.right(60)
        else:
            print("Something wrong in your entered command.")
            return


command = AXIOM
command = create_l_system(command)

t.tracer(0, 0)
t.hideturtle()

t.up()
t.goto(-(160 / 2), (160 / 2) / 3 ** 0.5)
t.down()

draw_l_system(command)
t.update()
t.done()
