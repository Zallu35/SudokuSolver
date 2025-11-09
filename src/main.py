import Board
import re
from tkinter import *
from tkinter import ttk

def main():
    
    def p_vals():
        for C in Cell_list:
            if C.get():
                print(f"{C}:{C.get()}")

    def update_entry():
        Cell_list[40].insert(0, 5)
    
    def clear_board():
        for Cell in Cell_list:
            Cell.delete(0)
    
    def entry_restriction(value):
        return re.match('^[0-9]*$', value) is not None and len(value) <2
    
        
    root = Tk()
    root.title("Sudoku Solver")
    sudoku_board = ttk.Frame(root)
    sudoku_board.grid(column=0, row=0, padx=4, pady=4, sticky=(N,W,E,S))
    solve = ttk.Button(root, text = "Solve", command=update_entry)
    solve.grid(column=0, row=1, sticky=(E))
    clear_board = ttk.Button(root, text="Clear", command=clear_board)
    clear_board.grid(column=0, row=1, sticky=(W))
    test_vals = ttk.Button(root, text="Vals", command=p_vals)
    test_vals.grid(column=0, row=1)
    valid_entry = (root.register(entry_restriction), '%P')
    
    Cell_list = []
    Value_list = []
    for i in range(1, 10): #row
        for j in range(1, 10): #column
            ValueID = StringVar()
            Value_list.append(ValueID)
            CellID = ttk.Entry(sudoku_board, justify = "center", width=3, textvariable=ValueID, validate='key', validatecommand=valid_entry)
            CellID.grid(column=j, row=i)
            Cell_list.append(CellID)
            

    #for v in Value_list:
        #pos=list(v)
        #c = ttk.Entry(sudoku_board, justify = "center", width=3, textvariable=v)
        #c.grid(column=int(pos[3]), row=int(pos[2]))
        #Cell_list.append(c)
    # CV=StringVar()
    #C=ttk.Entry(sudoku_board, textvariable=CV)
    #C.grid(column=0, row=0)
    #print(Cell_list[0].configure())
    #print(Value_list)
    root.mainloop() 

    
    



main()