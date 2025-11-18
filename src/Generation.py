import re
import Board
import tkinter as tk

def create_elements(): #relic of an earlier idea, unused currently and likely to be deleted
    Gameboard = Board()
    Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9 = Row(), Row(), Row(), Row(), Row(), Row(), Row(), Row(), Row()
    Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8, Column9 = Column(), Column(), Column(), Column(), Column(), Column(), Column(), Column(), Column()
    Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9 = Box(), Box(), Box(), Box(), Box(), Box(), Box(), Box(), Box()
    Cell11, Cell12, Cell13, Cell14, Cell15, Cell16, Cell17, Cell18, Cell19 = Cell(Row1, Column1, Box1), Cell(Row1, Column2, Box1), Cell(Row1, Column3, Box1), Cell(Row1, Column4, Box2), Cell(Row1, Column5, Box2), Cell(Row1, Column6, Box2), Cell(Row1, Column7, Box3), Cell(Row1, Column8, Box3), Cell(Row1, Column9, Box3)
    Cell21, Cell22, Cell23, Cell24, Cell25, Cell26, Cell27, Cell28, Cell29 = Cell(Row2, Column1, Box1), Cell(Row2, Column2, Box1), Cell(Row2, Column3, Box1), Cell(Row2, Column4, Box2), Cell(Row2, Column5, Box2), Cell(Row2, Column6, Box2), Cell(Row2, Column7, Box3), Cell(Row2, Column8, Box3), Cell(Row2, Column9, Box3)
    Cell31, Cell32, Cell33, Cell34, Cell35, Cell36, Cell37, Cell38, Cell39 = Cell(Row3, Column1, Box1), Cell(Row3, Column2, Box1), Cell(Row3, Column3, Box1), Cell(Row3, Column4, Box2), Cell(Row3, Column5, Box2), Cell(Row3, Column6, Box2), Cell(Row3, Column7, Box3), Cell(Row3, Column8, Box3), Cell(Row3, Column9, Box3)
    Cell41, Cell42, Cell43, Cell44, Cell45, Cell46, Cell47, Cell48, Cell49 = Cell(Row4, Column1, Box4), Cell(Row4, Column2, Box4), Cell(Row4, Column3, Box4), Cell(Row4, Column4, Box5), Cell(Row4, Column5, Box5), Cell(Row4, Column6, Box5), Cell(Row4, Column7, Box6), Cell(Row4, Column8, Box6), Cell(Row4, Column9, Box6)
    Cell51, Cell52, Cell53, Cell54, Cell55, Cell56, Cell57, Cell58, Cell59 = Cell(Row5, Column1, Box4), Cell(Row5, Column2, Box4), Cell(Row5, Column3, Box4), Cell(Row5, Column4, Box5), Cell(Row5, Column5, Box5), Cell(Row5, Column6, Box5), Cell(Row5, Column7, Box6), Cell(Row5, Column8, Box6), Cell(Row5, Column9, Box6)
    Cell61, Cell62, Cell63, Cell64, Cell65, Cell66, Cell67, Cell68, Cell69 = Cell(Row6, Column1, Box4), Cell(Row6, Column2, Box4), Cell(Row6, Column3, Box4), Cell(Row6, Column4, Box5), Cell(Row6, Column5, Box5), Cell(Row6, Column6, Box5), Cell(Row6, Column7, Box6), Cell(Row6, Column8, Box6), Cell(Row6, Column9, Box6)
    Cell71, Cell72, Cell73, Cell74, Cell75, Cell76, Cell77, Cell78, Cell79 = Cell(Row7, Column1, Box7), Cell(Row7, Column2, Box7), Cell(Row7, Column3, Box7), Cell(Row7, Column4, Box8), Cell(Row7, Column5, Box8), Cell(Row7, Column6, Box8), Cell(Row7, Column7, Box9), Cell(Row7, Column8, Box9), Cell(Row7, Column9, Box9)
    Cell81, Cell82, Cell83, Cell84, Cell85, Cell86, Cell87, Cell88, Cell89 = Cell(Row8, Column1, Box7), Cell(Row8, Column2, Box7), Cell(Row8, Column3, Box7), Cell(Row8, Column4, Box8), Cell(Row8, Column5, Box8), Cell(Row8, Column6, Box8), Cell(Row8, Column7, Box9), Cell(Row8, Column8, Box9), Cell(Row8, Column9, Box9)
    Cell91, Cell92, Cell93, Cell94, Cell95, Cell96, Cell97, Cell98, Cell99 = Cell(Row9, Column1, Box7), Cell(Row9, Column2, Box7), Cell(Row9, Column3, Box7), Cell(Row9, Column4, Box8), Cell(Row9, Column5, Box8), Cell(Row9, Column6, Box8), Cell(Row9, Column7, Box9), Cell(Row9, Column8, Box9), Cell(Row9, Column9, Box9)

def create_game(): #creates the initial game board
    board = []
    for x in range(9):
        board.append([])
        for y in range(9):
            board[x].append(0)
    return board
    
def fill_board(game, cells): #fills the given game board (matrix, list of lists) with the values input from the tkinter entry fields (it's a sudoku so there should be a total of 81)
    index=0
    x=0
    while x < 9:
        y=0
        while y < 9:
            if cells[index].get():
                game[x][y] = cells[index].get()
            else:
                game[x][y] = 0
            y+=1
            index+=1
        x+=1

def reset_board(entries): #clears all values from the tkinter entries
    for entry in entries:
            entry.delete(0)

def create_empty_cells_dict(game, cells, pot_dict): #creates the dictionary used to perform most of the solving logic based on the tkinter entriess
    index = 0
    for x in range(9):
        box_counter = 1
        if x > 2:
            box_counter = 4
        if x > 5:
            box_counter = 7
        for y in range(9):
            if y == 3:
                box_counter +=1
            if y == 6:
                box_counter +=1
            if game[x][y] == 0:
                pot_dict[f"{x}{y}"]=[cells[index], ['1','2','3','4','5','6','7','8','9'], box_counter]
            else:
                pot_dict[f"{x}{y}"]=[cells[index], [], box_counter]
            index+=1
            
            