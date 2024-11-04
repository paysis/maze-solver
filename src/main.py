from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(10, 10), Point(50, 50))
    line2 = Line(Point(70, 70), Point(100, 70))
    win.draw_line(line1, "black")
    win.draw_line(line2, "yellow")
    win.wait_for_close()

if __name__ == "__main__":
    main()