


def find_singles(potentials_dict):
    sing_lst = []
    for i in potentials_dict:
        if len(potentials_dict[i]) == 1:
            sing_lst.append(i)
    return sing_lst

def update_potentials(game, pot_dict, cell_index, boxes_dict):
    spl_index = list(cell_index)
    for value in game[int(spl_index[0])]:
        if value in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(value)
    for i in range(9):
        val = game[i][int(spl_index[1])] 
        if val in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(val)
    for value in boxes_dict[pot_dict[cell_index][2]]:
        v = pot_dict[value][0].get()
        if v in pot_dict[cell_index][1]:
            pot_dict[cell_index][1].remove(v)
