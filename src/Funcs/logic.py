


def fill_singles(game, pot_dict, boxes_dict):
    sing_lst = []
    for key in pot_dict:
        if len(pot_dict[key][1]) == 1:
            sing_lst.append(key)
    for cell in sing_lst:
        value = pot_dict[cell][1][0]
        insert_value(game, pot_dict, cell, boxes_dict, value)

def update_potentials(game, pot_dict, cell_index, boxes_dict):
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

def insert_value(game, pot_dict, cell_index, boxes_dict, new_value):
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
    print(cell_set)
    print(cells_to_update)
    for cell in cell_set:
        update_potentials(game, pot_dict, cell, boxes_dict)


