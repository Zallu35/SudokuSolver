from Generation import *
from tkinter import *
from tkinter import ttk

def test():
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
        
    def fill_board():
        index=0
        x=0
        while x < 9:
            y=0
            while y < 9:
                if Cell_list[index].get():
                    gb[x][y] = Cell_list[index].get()
                else:
                    gb[x][y] = 0
                y+=1
                index+=1
            x+=1
    
    def p_board():
        print(gb)
    

    root = Tk()
    root.title("Sudoku Solver")
    sudoku_board = ttk.Frame(root)
    sudoku_board.grid(column=0, row=0, padx=4, pady=4, sticky=(N,W,E,S))

    Cell_list = []
    Value_list = []
    valid_entry = (root.register(entry_restriction), '%P')
    for i in range(1, 10): #row
        for j in range(1, 10): #column
            ValueID = StringVar()
            Value_list.append(ValueID)
            CellID = ttk.Entry(sudoku_board, justify = "center", width=3, textvariable=ValueID, validate='key', validatecommand=valid_entry)
            CellID.grid(column=j, row=i)
            Cell_list.append(CellID)

    solve = ttk.Button(root, text = "Solve", command=fill_board)
    solve.grid(column=0, row=1, sticky=(E))
    clear_board = ttk.Button(root, text="Clear", command=clear_board)
    clear_board.grid(column=0, row=1, sticky=(W))
    test_vals = ttk.Button(root, text="Vals", command=p_vals)
    test_vals.grid(column=0, row=1)
    test_btn = ttk.Button(root, text="test", command=p_board)
    test_btn.grid(column=0, row=2)
    gb = create_game()

    
   
    
    
    root.mainloop() 

    
    


test()