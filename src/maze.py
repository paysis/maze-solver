from cell import Cell, WallType
from point import Point
from time import sleep

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.__create_cells()
    
    def __create_cells(self):
        self.__cells = []
        for i in range(self.num_cols):
            cells = []
            self.__cells.append(cells)
            for j in range(self.num_rows):
                c = Cell(self.win)
                cells.append(c)
                self.__draw_cell(i,j)
        self._break_entrance_and_exit()

    def __draw_cell(self, i, j):
        if i < 0:
            i = self.num_cols + i
        if j < 0:
            j = self.num_rows + j

        top_left = Point(
            self.x1 + (i * self.cell_size_x),
            self.y1 + (j * self.cell_size_y)
        )
        bottom_right = Point(
            top_left.x + self.cell_size_x,
            top_left.y + self.cell_size_y
        )
        self.__cells[i][j].set_top_left(top_left).set_bottom_right(bottom_right)
        if self.win != None:
            self.__cells[i][j].draw()

    def _break_entrance_and_exit(self):
        entry_cell = self.__cells[0][0]
        exit_cell = self.__cells[-1][-1]

        entry_cell.set_wall(WallType.TOP)
        exit_cell.set_wall(WallType.BOTTOM)

        self.__draw_cell(0, 0)
        self.__draw_cell(-1, -1)

    def __animate(self):
        self.win.redraw()
        sleep(0.05)

    def _get_cells(self):
        return self.__cells