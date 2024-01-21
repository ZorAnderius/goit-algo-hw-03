import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=420):
    wind = turtle.Screen()
    wind.bgcolor("black")
    
    turtle.TurtleScreen._RUNNING=True
    t = turtle.Turtle()
    t.color('white')
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 4)
    t.pendown()
    
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
        
    wind.mainloop()
    
def task2():
    while True:
        try:
            input_arg = int(input('Enter the level of recursion: (close to -1)):   ' ))
        except ValueError:
            print('Incorrect level of recursion. Please use positive numbers only')
            continue
        if input_arg ==-1:
            print('Good bye!')
            break
    
        if input_arg < 0:
            print('Incorrect level of recursion. Please use positive numbers or -1 for exit')
            continue
        
        draw_koch_snowflake(int(input_arg))

if __name__ == '__main__':
    task2()