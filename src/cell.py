from point import Point
from line import Line
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from window import Window

class WallType(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"

class Cell:
    def __init__(self, win):
        self.__win: Window = win
        self.__walls = {}
        self.top_left: Point = None
        self.bottom_right: Point = None

        self.set_wall(WallType.LEFT, True)
        self.set_wall(WallType.RIGHT, True)
        self.set_wall(WallType.TOP, True)
        self.set_wall(WallType.BOTTOM, True)

    def draw(self, fill_color="black"):
        if self.has_wall(WallType.LEFT):
            line = Line(Point(self.top_left.x, self.top_left.y), Point(self.top_left.x, self.bottom_right.y))
            self.__win.draw_line(line, fill_color)
        
        if self.has_wall(WallType.RIGHT):
            line = Line(Point(self.bottom_right.x, self.top_left.y), Point(self.bottom_right.x, self.bottom_right.y))
            self.__win.draw_line(line, fill_color)
        
        if self.has_wall(WallType.TOP):
            line = Line(Point(self.top_left.x, self.top_left.y), Point(self.bottom_right.x, self.top_left.y))
            self.__win.draw_line(line, fill_color)
        
        if self.has_wall(WallType.BOTTOM):
            line = Line(Point(self.top_left.x, self.bottom_right.y), Point(self.bottom_right.x, self.bottom_right.y))
            self.__win.draw_line(line, fill_color)


    def draw_move(self, to_cell, undo=False):
        self_center = Point(self.top_left.x + ((self.bottom_right.x - self.top_left.x) / 2), self.top_left.y + ((self.bottom_right.y - self.top_left.y) / 2))
        to_cell_center = Point(to_cell.top_left.x + ((to_cell.bottom_right.x - to_cell.top_left.x) / 2), to_cell.top_left.y + ((to_cell.bottom_right.y - to_cell.top_left.y) / 2))
        line = Line(self_center, to_cell_center)
        self.__win.draw_line(line, "gray" if undo else "red")

    def set_wall(self, wall: WallType, v: bool = False):
        if not isinstance(wall, WallType):
            raise ValueError("wall parameter must be an instance of WallType")
        self.__walls[wall.value] = v
        return self
    
    def has_wall(self, wall: WallType):
        if wall.value in self.__walls and self.__walls[wall.value]:
            return True
        return False

    def set_top_left(self, point: Point):
        self.top_left = point
        return self
    
    def set_bottom_right(self, point: Point):
        self.bottom_right = point
        return self