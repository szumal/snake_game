from collections import deque
from typing import Deque
import snakelib

width = 0  # initialized in play_snake
height = 0  # initialized in play_snake
ui = None  # initialized in play_snake
SPEED = 20
keep_running = True
initial_direction = 'r'

#def draw_snake(x,y):
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self)
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

def choose_place_4apple(snakelen, board):
    apple_spot = ui.random(height*width - snakelen)
    #print(board)
    for i in range (height):
        for j in range (width):
            if board[i][j] == 0:    
                apple_spot -=1                
                if apple_spot == -1:
                    return(j,i)

def play_snake(init_ui):
    global width, height, ui, keep_running
    ui = init_ui
    width, height = ui.board_size()
    direction = initial_direction
    
    board = [[0 for i in range(width)]for j in range (height)]
    board[0][0] = 1
    board[0][1] = 1
    ui.place(0,0,ui.SNAKE)
    ui.place(1,0,ui.SNAKE)
    body_x = []
    body_y = []
    body_x.append(0)
    body_y.append(0)
    body_x.append(1)
    body_y.append(0)  
    current_x = 1
    current_y = 0
    applex, appley = choose_place_4apple(2, board)
    ui.place(applex, appley, ui.FOOD)
    board[appley][applex] = 2
    ui.show()

    while keep_running:
        event = ui.get_event()
        print(event.name + " : " + event.data)
        
        if event.name == "arrow":
            if event.data == 'r' and direction != 'l': 
                direction = event.data
            if event.data == 'l' and direction != 'r': 
                direction = event.data
            if event.data == 'u' and direction != 'd': 
                direction = event.data
            if event.data == 'd' and direction != 'u': 
                direction = event.data

        
        if event.name == "alarm":
            if direction == 'r':current_x +=1                
            if direction == 'l':current_x -=1                
            if direction == 'u':current_y -=1
            if direction == 'd':current_y +=1
                
            current_x %= width
            current_y %= height
            body_x.append(current_x)
            body_y.append(current_y) 
            
            if board[current_y][current_x] == 2:
                applex, appley = choose_place_4apple(len(body_x), board)
                ui.place(applex, appley, ui.FOOD)
                board[appley][applex] = 2       
            else:
                tail_x = body_x[0]
                tail_y = body_y[0]
                body_x.pop(0)
                body_y.pop(0)
                board[tail_y][tail_x] = 0
                ui.place(tail_x, tail_y, ui.EMPTY)


                if board[current_y][current_x] == 1:
                     ui.set_game_over()
                     ui.show()  
            board[current_y][current_x] = 1
            ui.place(current_x, current_y, ui.SNAKE)
            print(board)
            ui.show()
            
         
            

        # make sure you handle the quit event like below,
        # or the test might get stuck in an infinite loop
        if event.name == "quit":
            keep_running = False


if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(20, 20)
    ui.set_animation_speed(10)
    play_snake(ui)
