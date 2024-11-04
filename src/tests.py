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
        num_cols = 120
        num_rows = 100
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
        m1._break_entrance_and_exit()
        cells = m1._get_cells()
        entry_c = cells[0][0]
        exit_c = cells[-1][-1]

        self.assertEqual(entry_c.has_wall(WallType.TOP), False)
        self.assertEqual(entry_c.has_wall(WallType.BOTTOM), True)
        self.assertEqual(entry_c.has_wall(WallType.RIGHT), True)
        self.assertEqual(entry_c.has_wall(WallType.LEFT), True)

        self.assertEqual(exit_c.has_wall(WallType.TOP), True)
        self.assertEqual(exit_c.has_wall(WallType.BOTTOM), False)
        self.assertEqual(exit_c.has_wall(WallType.RIGHT), True)
        self.assertEqual(exit_c.has_wall(WallType.LEFT), True)

if __name__ == "__main__":
    unittest.main()