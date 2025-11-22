import turtle
import random
import time

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Turtle Location Game")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.speed(0)
drawing_board.tracer(0)

turtle_instance.penup()

start_time = time.time()

def moveRandom():
    now = time.time()
    if now - start_time >= 15:
        return
    turtle_instance.goto(random.randint(-200, 200), random.randint(-200, 200))
    drawing_board.update()
    drawing_board.ontimer(moveRandom, 800)

drawing_board.ontimer(moveRandom, 500)

clickNumberTurtle =0
def update_score():
    write.clear()
    write.write("Score " + str(clickNumberTurtle),
                align="center",
                font=("Arial", 20, "bold"))
    drawing_board.update()
def clicktheTurtle(x,y):
    global clickNumberTurtle
    if time.time()-start_time >= 15:
        return
    clickNumberTurtle += 1
    update_score()

def timeTurtle():
    elapsed = int(-15 + (time.time() - start_time))

    if elapsed > 0:
        time_writer.clear()
        drawing_board.update()
        return
    time_writer.clear()
    time_writer.write("Time: " + str(-elapsed),
                      align="center",
                      font=("Arial", 16, "normal"))
    drawing_board.update()
    drawing_board.ontimer(timeTurtle, 1000)


print()
write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(0,260)
turtle_instance.onclick(clicktheTurtle)
update_score()

time_writer = turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(0,240)

timeTurtle()




print("completed")





turtle.mainloop()

