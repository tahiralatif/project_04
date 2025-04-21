# graphics.py - John Zelle's simple graphics module for Python

from tkinter import Canvas as TkCanvas, Tk


class GraphicsError(Exception): pass

class Canvas:
    def __init__(self, width, height):
        self.tk = Tk()
        self.canvas = TkCanvas(self.tk, width=width, height=height)

        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.canvas.bind("<Motion>", self._motion)
        self.canvas.bind("<Button-1>", self._click)
        self.last_click = None
        self.tk.update()

    def _motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _click(self, event):
        self.last_click = (event.x, event.y)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def get_last_click(self):
        return self.last_click

    def wait_for_click(self):
        while self.last_click is None:
            self.tk.update()

    def create_rectangle(self, x1, y1, x2, y2, color='blue'):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color, outline=color)

    def moveto(self, obj, x, y):
        coords = self.canvas.coords(obj)
        if coords:
            dx = x - coords[0]
            dy = y - coords[1]
            self.canvas.move(obj, dx, dy)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def update(self):
        self.tk.update()