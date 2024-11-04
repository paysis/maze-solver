class Line:
    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_x.x,
            self.point_x.y,
            self.point_y.x,
            self.point_y.y,
            fill=fill_color,
            width=2
        )