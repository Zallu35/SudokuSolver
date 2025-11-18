
"""
The original idea I had was to store everything in a variety of classes and run the logic through methods. I also wasn't going to have a user interface and just have all fields entered via CLI.
I have since changed my mind on how I wanted to do this and do not use any of this code at the moment. I didn't want to delete it in case any of it wound up being useful in the future but it's likely to be removed at the end of the project
"""

class Board:
    def __init__(self):
        self.complete = False
        self.incomplete_rows = []
        self.incomplete_boxes = []
        self.incomplete_columns = []

class Cell:
    def __init__(self, row, column, box):
        self.row = row
        self.column = column
        self.box = box
        self.value = 0
        self.potential = []
    
    def update_value(self, value):
        self.value = value
        self.potential.clear()

    def add_potentials(self, potentials_list):
        self.potential = potentials_list
    
    def remove_potential(self, value):
        self.potential.remove(value)

class Row:
    def __init__(self):
        self.boxes = []
        self.columns = []
        self.cells = []
        self.empty = [] #list of empty cells (value = 0)
    
    def fill_boxes(self, box):
        self.boxes.append(box)

    def fill_columns(self, column):
        self.columns.append(column)

    def fill_cells(self, cell):
        self.cells.append(cell)

class Box:
    def __init__(self):
        self.rows = []
        self.columns = []
        self.cells = []
        self.empty = [] #list of empty cells (value = 0)

    def fill_rows(self, row):
        self.rows.append(row)

    def fill_columns(self, column):
        self.columns.append(column)

    def fill_cells(self, cell):
        self.cells.append(cell)

class Column:
    def __init__(self):
        self.rows = []
        self.boxes = []
        self.cells = []
        self.empty = [] #list of empty cells (value = 0)

    def fill_boxes(self, box):
        self.boxes.append(box)

    def fill_rows(self, row):
        self.rows.append(row)

    def fill_cells(self, cell):
        self.cells.append(cell)