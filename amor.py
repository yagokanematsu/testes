import turtle

# Configurações iniciais
t = turtle.Turtle()
t.speed(3)
t.color("red")
t.pensize(5)

# Função para mover sem desenhar
def pula(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Desenhar letra Y
def letra_Y():
    t.left(60)
    t.forward(60)
    t.backward(60)
    t.right(120)
    t.forward(60)
    t.backward(60)
    t.left(60)
    t.forward(60)

# Desenhar letra A
def letra_A():
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    t.backward(50)
    t.right(110)
    t.forward(35)
    t.backward(35)
    t.left(110)
    t.forward(50)
    t.left(70)

# Desenhar letra G
def letra_G():
    t.circle(40, 270)
    t.forward(40)
    t.backward(20)
    t.right(90)
    t.forward(30)
    t.left(90)

# Desenhar letra O
def letra_O():
    t.circle(40)

# Desenhar coração
def coracao():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# --- DESENHO ---

# Y
pula(-300, 0)
letra_Y()

# A
pula(-200, 0)
letra_A()

# G
pula(-60, 0)
letra_G()

# O
pula(80, 0)
letra_O()

# Coração
t.color("red")
t.pensize(3)
pula(250, -50)
coracao()

# Finaliza
t.hideturtle()
turtle.done()