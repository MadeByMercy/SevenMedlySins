'''
The functions for Seven Medley Sins
'''

import tkinter as tk

### --- These are the functions for saving and loading files --- ###
def save_func(save_file,data):
    try:
        file = open(save_file,"x")
        file.close()
    except FileExistsError:
        file = open(save_file,"w")
        file.write(data)
        file.close()

def load_func(save_file):
    file = open(save_file,"r")
    game_values = file.read()
    file.close()
    return game_values

### --- This is the data which has to be saved --- ###
# Each data value will have its own file to be written to
player_health = str("A given value")
position = str("Given value of x,Given value of y")
weaponry = str("Some Given Values")
upgrades = str("Number of upgrades per weapon")
inventory = str("Item Number , Number of item")
inventory_dict = {}
currency = str("Similar to health one value that gets stringed")

### --- This is so that the mouse can be tracked and therefore the player can shoot in 360 degrees --- ###
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()