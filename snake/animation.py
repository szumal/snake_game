import snakelib

width = 0  # initialized in play_animation
height = 0  # initialized in play_snake
ui = None  # initialized in play_animation
SPEED = 20
keep_running = True
change = False

def draw(x,y):
    ui.clear()
    ui.place(x,y,ui.SNAKE)
    ui.show()

def draw_apple(x,y):
    ui.clear()
    ui.place(x,y,ui.FOOD)
    ui.show()


def play_animation(init_ui):
    global width, height, ui, keep_running, change
    ui = init_ui
    width, height = ui.board_size()
    draw(0,0)
    i,j = 1,0
    while keep_running:
        event = ui.get_event()
        print(event.name + " : " + event.data)
        print(change)
        if i > width-1: i = 0; j+=1
        if j > height-1: j = 0
        
        if event.name == 'other' and event.data == 'space':
            change = True if change == False else False

        if change == True and event.name == 'alarm':
            draw_apple(i,j)
            i +=1
        if change == False and event.name == "alarm":
            draw(i,j)
            i +=1


        # make sure you handle the quit event like below,
        # or the test might get stuck in an infinite loop
        if event.name == "quit":
            keep_running = False

if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(20, 20)
    ui.set_animation_speed(3)
    play_animation(ui)
