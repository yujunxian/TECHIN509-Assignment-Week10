import unittest
from models.board import Board  

class TestCheckWinner(unittest.TestCase):
    def test_row_winner(self):
        b = Board()
        b.grid = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(b.check_winner(), "X")  

    def test_column_winner(self):
        b = Board()
        b.grid = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
        self.assertEqual(b.check_winner(), "X") 

    def test_diagonal_winner(self):
        b = Board()
        b.grid = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(b.check_winner(), "X")  

    def test_no_winner(self):
        b = Board()
        b.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertEqual(b.check_winner(), "")  

if __name__ == "__main__":
    unittest.main()
