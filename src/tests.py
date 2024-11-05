import unittest

from maze import Maze
from cell import WallType

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        cells = m1._get_cells()
        self.assertEqual(
            len(cells),
            num_cols
        )
        self.assertEqual(
            len(cells[0]),
            num_rows
        )
    
    def test_maze_create_cells_with_nonzero_location(self):
        num_cols = 24
        num_rows = 10
        m1 = Maze(100, 200, num_rows, num_cols, 10, 20)
        cells = m1._get_cells()
        self.assertEqual(
            len(cells),
            num_cols
        )
        self.assertEqual(
            len(cells[0]),
            num_rows
        )

    def test_maze_entrance_and_exit_exists(self):
        m1 = Maze(0,0,12,12,20,20)
        cells = m1._get_cells()
        entry_c = cells[0][0]
        exit_c = cells[-1][-1]

        self.assertEqual(entry_c.has_wall(WallType.TOP), False)
        self.assertEqual(exit_c.has_wall(WallType.BOTTOM), False)

    def test_reset_cells(self):
        m1 = Maze(0,0,12,12,20,20)
        cells = m1._get_cells()

        self.assertEqual(
            cells[0][0].visited,
            False
        )
        self.assertEqual(
            cells[5][5].visited,
            False
        )
        self.assertEqual(
            cells[-1][-1].visited,
            False
        )


if __name__ == "__main__":
    unittest.main()