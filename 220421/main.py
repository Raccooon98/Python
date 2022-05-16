from tkinter import *
import table, ball

x_velocity = 10
y_velocity = 10

window =Tk()
window.title("MyPong")

my_table = table.Table(window, net_colour="green",vertical_net=True)

my_ball = ball.Ball(table=my_table,x_speed=x_velocity,y_speed=y_velocity,width=24,height=24,colour="red",x_start=288,y_start=188)
def game_flow():
    my_ball.move_next()
    window.after(50, game_flow)

game_flow()

window.mainloop()