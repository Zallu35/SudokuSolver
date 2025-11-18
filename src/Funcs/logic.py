


def fill_singles(game, pot_dict, boxes_dict): #scans potentials dictionary for any cells with only one potential value and fills it in
    sing_lst = []
    for key in pot_dict:
        if len(pot_dict[key][1]) == 1:
            sing_lst.append(key)
    for cell in sing_lst:
        value = pot_dict[cell][1][0]
        insert_value(game, pot_dict, cell, boxes_dict, value)

def update_potentials(game, pot_dict, cell_index, boxes_dict): #updates an individual cell's potentials list based on the current state of the board
    split_index = list(cell_index)
    for value in game[int(split_index[0])]:
        if value in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(value)
    for row in range(9):
        val = game[row][int(split_index[1])] 
        if val in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(val)
    for value in boxes_dict[pot_dict[cell_index][2]]:
        v = pot_dict[value][0].get()
        if v in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(v)

def insert_value(game, pot_dict, cell_index, boxes_dict, new_value): #inserts a value into a cell and calls update_potentials on any cell it can affect
    split_index = list(cell_index)
    game[int(split_index[0])][int(split_index[1])] = new_value
    pot_dict[cell_index][0].insert(0, new_value)
    pot_dict[cell_index][1].clear()
    cells_to_update = []
    column_counter = 0
    for value in game[int(split_index[0])]:
        if value == 0:
            index_to_add = split_index[0] + str(column_counter)
            cells_to_update.append(index_to_add)
        column_counter +=1
    for row in range(9):
        val = game[row][int(split_index[1])] 
        if val == 0:
            index_to_add = str(row)+split_index[1]
            cells_to_update.append(index_to_add)
    box_cells = boxes_dict[(pot_dict[cell_index][2])]
    for cell in box_cells:
        if pot_dict[cell][0].get() == 0:
            cells_to_update.append(cell)
    cell_set = set(cells_to_update) #this removes duplicates if there are any
    for cell in cell_set:
        update_potentials(game, pot_dict, cell, boxes_dict)

def potentials_row_scan(game, pot_dict, boxes_dict): #scans all rows for isolated potentials (only one instance of a potential value) and fills them if any are found
    for row in range(9):
        row_cells = []
        for column in range(9):
            cellID = str(row)+str(column)
            if not pot_dict[cellID][0].get():
                row_cells.append(cellID)
        scanning_list = []
        for cell in row_cells:
            cell_potentials = pot_dict[cell][1]
            if len(cell_potentials)>0:
                scanning_list.extend(cell_potentials)
        filling_list = []
        for val in range(1,10):
            if scanning_list.count(str(val)) == 1:
                filling_list.append(str(val))
        if len(filling_list)>0:
            for fill in filling_list:
                for item in row_cells:
                    if fill in pot_dict[item][1]:
                        insert_value(game, pot_dict, item, boxes_dict, int(fill))
                        row_cells.remove(item)

def potentials_column_scan(game, pot_dict, boxes_dict): #scans all columns for isolated potentials (only one instance of a potential value) and fills them if any are found
    for column in range(9):
        column_cells = []
        for row in range(9):
            cellID = str(row)+str(column)
            if not pot_dict[cellID][0].get():
                column_cells.append(cellID)
        scanning_list = []
        for cell in column_cells:
            cell_potentials = pot_dict[cell][1]
            if len(cell_potentials)>0:
                scanning_list.extend(cell_potentials)
        filling_list = []
        for val in range(1,10):
            if scanning_list.count(str(val)) == 1:
                filling_list.append(str(val))
        if len(filling_list)>0:
            for fill in filling_list:
                for item in column_cells:
                    if fill in pot_dict[item][1]:
                        insert_value(game, pot_dict, item, boxes_dict, int(fill))
                        column_cells.remove(item)

def potentials_box_scan(game, pot_dict, boxes_dict): #scans all boxes for isolated potentials (only one instance of a potential value) and fills them if any are found
    for key in range(1,10):
        box_cells = []
        ref_cells = boxes_dict[key]
        print(ref_cells)
        for cellID in ref_cells:
            #print(cellID)
            #print(pot_dict[cellID][0].get())
            if not pot_dict[cellID][0].get():
                box_cells.append(cellID)
        print(box_cells)
        scanning_list = []
        for cell in box_cells:
            cell_potentials = pot_dict[cell][1]
            if len(cell_potentials)>0:
                scanning_list.extend(cell_potentials)
        print(scanning_list)
        filling_list = []
        for val in range(1,10):
            if scanning_list.count(str(val)) == 1:
                filling_list.append(str(val))
        print(filling_list)
        if len(filling_list)>0:
            for fill in filling_list:
                for item in box_cells:
                    if fill in pot_dict[item][1]:
                        insert_value(game, pot_dict, item, boxes_dict, int(fill))
                        box_cells.remove(item)
