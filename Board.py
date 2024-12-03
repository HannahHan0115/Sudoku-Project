import pygame
from Cell import Cell
import numpy as np

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected = None

    def draw(self):
        # Draw Sudoku grid outline
        # Draw every cell on the board
        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        self.selected = (row, col)

    def click(self, x, y):
        for i in range(9):
            for j in range(9):
                if x >= i * 50 and x < (i + 1) * 50 and y >= j * 50 and y < (j + 1) * 50:
                    return (i, j)
        return None

    def clear(self):
        if self.selected:
            self.cells[self.selected[1]][self.selected[0]].set_cell_value(0)

    def sketch(self, value):
        if self.selected:
            self.cells[self.selected[1]][self.selected[0]].set_sketched_value(value)

    def place_number(self, value):
        if self.selected:
            self.cells[self.selected[1]][self.selected[0]].set_cell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                # Reset cell to original value
                cell.set_cell_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        for row in self.cells:
            for cell in row:
                cell.update()

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None

    def check_board(self):
            # Check rows
        for row in self.cells:
            values = [cell.value for cell in row if cell.value != 0]
            if len(values) != len(set(values)):
                return False

        # Check columns
        for col in range(9):
            values = [self.cells[row][col].value for row in range(9) if self.cells[row][col].value != 0]
            if len(values) != len(set(values)):
                return False

            # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                values = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if self.cells[row][col].value != 0:
                            values.append(self.cells[row][col].value)
                if len(values) != len(set(values)):
                    return False

        return True
        # Implementation to check if the Sudoku board is solved correctly
        pass