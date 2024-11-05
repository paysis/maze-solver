from window import Window
from line import Line
from point import Point
from cell import Cell, WallType
from maze import Maze

def main():
    win = Window(800, 600)
    m1 = Maze(10,10,12,10,20,20,win)
    m1.solve_bfs()
    win.wait_for_close()

if __name__ == "__main__":
    main()