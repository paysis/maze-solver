from window import Window
from line import Line
from point import Point
from cell import Cell, WallType

def main():
    win = Window(800, 600)
    cell1 = Cell(win) \
                .set_top_left(Point(10, 10)) \
                .set_bottom_right(Point(30, 30))
    cell2 = Cell(win) \
                .set_top_left(Point(30, 10)) \
                .set_bottom_right(Point(50, 30)) 
    cell3 = Cell(win) \
                .set_top_left(Point(60, 30)) \
                .set_bottom_right(Point(110, 90)) 
    
    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()