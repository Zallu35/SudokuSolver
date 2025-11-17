import Board
import re
from tkinter import *
from tkinter import ttk
from Generation import *
from Funcs import logic

def main():
    
    def print_vals():
        for C in Cell_list:
            if C.get():
                print(f"{C}:{C.get()}") 
        for key in potentials:
            print(key, potentials[key][1])

    def solve_action():
        fill_board(gb, Cell_list)
        create_empty_cells_dict(gb, Cell_list, potentials)
        for cell in potentials:
            if potentials[cell][1]:
                logic.update_potentials(gb, potentials, cell, boxes)
        logic.fill_singles(gb, potentials, boxes)
    
    def clear_board():
        reset_board(Cell_list)
        create_empty_cells_dict(gb, Cell_list, potentials)
    
    def entry_restriction(value):
        return re.match('^[0-9]*$', value) is not None and len(value) <2

    def t1():
        logic.insert_value(gb, potentials, cell_index, boxes, new_value)

    def t2():
        logic.update_potentials(gb, potentials, '02', boxes)
    
    def t3():
        for key in potentials:
            print(key, potentials[key][1])
        print(gb)
    
        
    root = Tk()
    root.title("Sudoku Solver")
    sudoku_board = ttk.Frame(root)
    sudoku_board.grid(column=0, row=0, padx=4, pady=4, sticky=(N,W,E,S))
    
    valid_entry = (root.register(entry_restriction), '%P')
    
    Cell_list = []
    Value_list = []

    for i in range(9): #row
        for j in range(9): #column
            ValueID = StringVar()
            Value_list.append(ValueID)
            CellID = ttk.Entry(sudoku_board, justify = "center", width=3, textvariable=ValueID, validate='key', validatecommand=valid_entry)
            CellID.grid(column=j, row=i)
            Cell_list.append(CellID)

    gb = create_game()
    boxes = {
        1:['00', '01', '02', '10', '11', '12', '20', '21', '22'],
        2:['03', '04', '05', '13', '14', '15', '23', '24', '25'],
        3:['06', '07', '08', '16', '17', '18', '26', '27', '28'],
        4:['30', '31', '32', '40', '41', '42', '50', '51', '52'],
        5:['33', '34', '35', '43', '44', '45', '53', '54', '55'],
        6:['36', '37', '38', '46', '47', '48', '56', '57', '58'],
        7:['60', '61', '62', '70', '71', '72', '80', '81', '82'],
        8:['63', '64', '65', '73', '74', '75', '83', '84', '85'],
        9:['66', '67', '68', '76', '77', '78', '86', '87', '88']
    }
    potentials = {}
            
    solve = ttk.Button(root, text = "Solve", command=solve_action)
    solve.grid(column=0, row=1, sticky=(E))
    clear_board = ttk.Button(root, text="Clear", command=clear_board)
    clear_board.grid(column=0, row=1, sticky=(W))
    test_vals = ttk.Button(root, text="Vals", command=print_vals)
    test_vals.grid(column=0, row=1)
    test_f1 = ttk.Button(root, text="One", command=t1)
    test_f1.grid(column=1, row=0, sticky=(N))
    test_f2 = ttk.Button(root, text="Two", command=t2)
    test_f2.grid(column=1, row=0)
    test_f3 = ttk.Button(root, text="Three", command=t3)
    test_f3.grid(column=1, row=0, sticky=(S))


    root.mainloop() 

    

main()