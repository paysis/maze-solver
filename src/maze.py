from cell import Cell, WallType
from point import Point
from time import sleep
import random

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
            seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed:
            random.seed(seed)

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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while 1:
            to_visit = []
            
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            direction = random.randrange(0, len(to_visit))
            v_i, v_j = to_visit[direction]
            # remember: i is of columns and j is of rows
            # so keeping i same and changing j means
            # its now vertical as two items are in same column
            # and different rows
            if v_i == i + 1:
                self.__cells[i][j].set_wall(WallType.RIGHT)
                self.__cells[v_i][v_j].set_wall(WallType.LEFT)
            elif v_i == i - 1:
                self.__cells[i][j].set_wall(WallType.LEFT)
                self.__cells[v_i][v_j].set_wall(WallType.RIGHT)
            elif v_j == j + 1:
                self.__cells[i][j].set_wall(WallType.BOTTOM)
                self.__cells[v_i][v_j].set_wall(WallType.TOP)
            elif v_j == j - 1:
                self.__cells[i][j].set_wall(WallType.TOP)
                self.__cells[v_i][v_j].set_wall(WallType.BOTTOM)

            self._break_walls_r(v_i, v_j)
            
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False

    def solve_bfs(self):
        start = (0, 0)
        end = (self.num_cols-1, self.num_rows-1)
        visited_paths = [[start]]
        visited = set()
        while len(visited_paths):
            path = visited_paths.pop(0)
            i, j = path[-1]
            cell = self.__cells[i][j]
            if not (i == 0 and j == 0):
                b_i, b_j = path[-2]
                cell.draw_move(self.__cells[b_i][b_j])

            if path[-1] == end:
                return True

            if i > 0 and not cell.has_wall(WallType.LEFT) and not self.__cells[i - 1][j].has_wall(WallType.RIGHT) and (i-1, j) not in visited:
                visited_paths.append(path + [(i-1, j)])
                visited.add((i-1, j))
            if i < self.num_cols-1 and not cell.has_wall(WallType.RIGHT) and not self.__cells[i + 1][j].has_wall(WallType.LEFT) and (i+1, j) not in visited:
                visited_paths.append(path + [(i+1, j)])
                visited.add((i+1, j))
            if j > 0 and not cell.has_wall(WallType.TOP) and not self.__cells[i][j - 1].has_wall(WallType.BOTTOM) and (i, j-1) not in visited:
                visited_paths.append(path + [(i, j - 1)])
                visited.add((i, j - 1))
            if j < self.num_rows-1 and not cell.has_wall(WallType.BOTTOM) and not self.__cells[i][j + 1].has_wall(WallType.TOP) and (i, j+1) not in visited:
                visited_paths.append(path + [(i, j + 1)])
                visited.add((i, j + 1))
                
            self.__animate()
        return False


    def solve_dfs(self):
        r = self._solve_r(0, 0)
        return r

    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        # right direction
        if i < self.num_cols - 1 and not self.__cells[i][j].has_wall(WallType.RIGHT) and not self.__cells[i + 1][j].has_wall(WallType.LEFT) and not self.__cells[i + 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            r = self._solve_r(i + 1, j)
            if r:
                return r
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)

        
        # left direction
        if i > 0 and not self.__cells[i][j].has_wall(WallType.LEFT) and not self.__cells[i - 1][j].has_wall(WallType.RIGHT) and not self.__cells[i - 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            r = self._solve_r(i - 1, j)
            if r:
                return r
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)

        # bottom direction
        if j < self.num_rows - 1 and not self.__cells[i][j].has_wall(WallType.BOTTOM) and not self.__cells[i][j + 1].has_wall(WallType.TOP) and not self.__cells[i][j + 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            r = self._solve_r(i, j + 1)
            if r:
                return r
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)

        # top direction
        if j > 0 and not self.__cells[i][j].has_wall(WallType.TOP) and not self.__cells[i][j - 1].has_wall(WallType.BOTTOM) and not self.__cells[i][j - 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            r = self._solve_r(i, j - 1)
            if r:
                return r
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)

        return False

    def __animate(self):
        self.win.redraw()
        sleep(0.1)

    def _get_cells(self):
        return self.__cells