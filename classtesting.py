import random
import time


class Game():
    pass


class Gameboard():
    def __init__(self, height, width, start):
        self.start = start
        self.x, self.y = start
        self.height = height
        self.width = width
        # self.margin
        self.gameboard = self.build_gameboard()
        self.blank = ""
        self.terminal = Terminal()
        self.terminal.clear_screen()

    def get_gameboard(self):
        return self.gameboard

    def build_gameboard(self):
        gameboard = []
        for x in range(self.height):
            line = []
            for y in range(self.width):
                line.append(Pixel())
            gameboard.append(line)
        return gameboard

    def draw_gameboard(self):
        # self.terminal.clear_screen()
        self.terminal.hide_cursor()
        x, y = self.start
        start = y
        for line in self.gameboard:
            y = start
            for pixel in line:
                self.terminal.set_position((x, y))
                if pixel.visible and pixel.changed:
                    pixel.set_changed()
                    color = pixel.color
                    background = pixel.background
                    self.terminal.set_color(pixel.color)
                    self.terminal.set_background(pixel.background)
                    print(pixel.get_character(), end="", flush=True)
                    y += 1
                else:
                    y += 1
            self.terminal.reset()
            # self.terminal.clear_right()
            x += 1
        # self.terminal.clear_left()
        self.terminal.show_cursor()

    def update_pixel(self, x, y, character, color, background):
        self.gameboard[x][y].set_color(color)
        self.gameboard[x][y].set_background(background)
        self.gameboard[x][y].set_character(character)

    def print_text(self, x, y, text, color, background):
        for character in text:
            gameboard.update_pixel(x, y, character, color, background)
            y += 1


class Pixel():
    visible = 1
    color = 15
    background = 10
    character = " "
    layer = 0
    changed = 1

    def __init__(self):
        self.visible = Pixel.visible
        self.color = Pixel.color
        self.background = Pixel.background
        self.character = Pixel.character
        self.layer = Pixel.layer
        self.changed = Pixel.changed

    def get_color(self):
        return self.color

    def get_visible(self):
        return self.visible

    def get_character(self):
        return self.character

    def set_color(self, color):
        self.changed = 1
        self.color = color

    # def show_pixel(self):
    #     self.character = 1

    def get_background(self):
        return self.background

    def set_background(self, color):
        self.changed = 1
        self.background = color

    def hide_pixel(self):
        self.visible = 0

    def set_character(self, character):
        self.changed = 1
        self.character = character

    def set_layer(self, layer):
        self.layer = layer

    def set_changed(self):
        self.changed = 0


class Terminal():

    def show_cursor(self):
        # This code shows the cursor
        print("\x1b[?25h", end="")

    def hide_cursor(self):
        # This code hides the cursor
        print("\x1b[?25l", end="")

    def set_position(self, coordinates):
        line, column = coordinates
        # This code sets the position of the cursor
        # in the terminal.
        print(f"\u001b[{line};{column}f", end="")

    def set_underline(self):
        print("\u001b[4m,", end="")

    def set_bold(self):
        print("\u001b[1m", end="")

    def get_color(self, color_code):
        return f"\u001b[38;5;{color_code}m"

    def set_color(self, color_code):
        color_code = self.get_color(color_code)
        print(color_code, end="")

    def get_background(self, color_code):
        return f"\u001b[48;5;{color_code}m"

    def set_background(self, color_code):
        color_code = self.get_background(color_code)
        print(color_code, end="")

    def set_random_color(self):
        # Sets a random color outside of the greyscale range
        color_code = random.randint(1, 231)
        self.set_color(color_code)

    def get_random_color(self):
        # Returns the code for a random color outside of the
        # greyscale range
        color_code = random.randint(1, 231)
        return color_code

    def reset(self):
        print("\u001b[0m")

    def clear_left(self):
        print("\u001b[1K")

    def clear_right(self):
        print("\u001b[0K")

    def clear_line(self):
        print("\u001b[2K")

    def clear_screen(self):
        print("\u001b[2J")


class Box():
    def __init__(self, coordinate1, coordinate2):
        self.x1, self.y1 = coordinate1
        self.x3, self.y3 = coordinate2
        self.x2, self.y4 = coordinate1
        self.x4, self.y2 = coordinate2

        self.upper_left = (self.x1, self.y1)
        self.upper_right = (self.x2, self.y2)
        self.lower_right = (self.x3, self.y3)
        self.lower_left = (self.x4, self.y4)
        self.height = self.x1 + self.x4
        self.width = self.y1 + self.y3
        # self.style = style  # style name
        # clear_screen()
        self.box_list = self.make_box_list()

    def calculate_area(self):
        return self.height * self.width

    def make_box_list(self):
        # This makes a clockwide list of x, y coordinates
        # starting in the top left
        box_list = []
        box_list.append(self.upper_left)
        # From upper_left to upper_right
        for y in range(self.y1+1, self.y2):
            box_list.append((self.x1, y))
        box_list.append(self.upper_right)
        # From upper_right to lower_right
        for x in range(self.x2+1, self.x3):
            box_list.append((x, self.y2))
        box_list.append(self.lower_right)
        # From lower_right to lower_left
        for y in range(self.y3-1, self.y1, -1):
            box_list.append((self.x3, y))
        box_list.append(self.lower_left)
        # From lower_left to upper_right
        for x in range(self.x4-1, self.x1, -1):
            box_list.append((x, self.y4))
        return box_list

    def get_box_list(self):
        return self.box_list

    def draw_box(self):
        for coordinates in self.box_list:
            x, y = coordinates
            print(x, y)
            print_text(x, y, "█", 11)

    def draw_bordered_box(self):
        for coordinates in self.box_list:
            pass


# class Style():
#     def __init__(self,
#                  name,
#                  top_left,
#                  top_right,
#                  horizontal,
#                  vertical,
#                  bottom_left,
#                  bottom_right):
#         self.name = name
#         self.top_left = top_left
#         self.top_right = top_right
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.bottom_left = bottom_left
#         self.bottom_right = bottom_right

#     def get_style(self):
#         return {
#             self.name: {
#                 "top_left": self.top_left,
#                 "top_right": self.top_right,
#                 "horizontal": self.horizontal,
#                 "vertical": self.vertical,
#                 "bottom_left": self.bottom_left,
#                 "bottom_right": self.bottom_right
#             }
#         }


gameboard = Gameboard(20, 40, (1, 10))
gameboard.draw_gameboard()

text = "Hello World!"
color = 15
background = 10
gameboard.print_text(6, 8, text, color, background)
text = "So nice to meet you."
color = 200
gameboard.print_text(7, 8, text, color, background)

text = "Hello World!"
color = 15
gameboard.draw_gameboard()
mybox = Box((0, 0), (19, 39))
mybox2 = Box((1, 1), (18, 38))
mybox3 = Box((2, 2), (17, 37))
mybox4 = Box((3, 3), (16, 36))

box_list = mybox.get_box_list()
box_list2 = mybox2.get_box_list()
box_list3 = mybox3.get_box_list()
box_list4 = mybox4.get_box_list()

sleep_time = .1
color = 1
for x in range(255):
    for coordinates in box_list4:
        x, y = coordinates
        gameboard.print_text(x, y, "█", color, background)
        # gameboard.draw_gameboard()
    time.sleep(sleep_time)
    gameboard.draw_gameboard()
    for coordinates in box_list3:
        x, y = coordinates
        gameboard.print_text(x, y, "█", color, background)
        # gameboard.draw_gameboard()
    time.sleep(sleep_time)
    gameboard.draw_gameboard()
    for coordinates in box_list2:
        x, y = coordinates
        gameboard.print_text(x, y, "█", color, background)
        # gameboard.draw_gameboard()
    time.sleep(sleep_time)
    gameboard.draw_gameboard()
    for coordinates in box_list:
        x, y = coordinates
        gameboard.print_text(x, y, "█", color, background)
        # gameboard.draw_gameboard()
    time.sleep(sleep_time)
    gameboard.draw_gameboard()
    color += 1
