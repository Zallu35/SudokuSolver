


def find_singles(potentials_dict):
    sing_lst = []
    for i in potentials_dict:
        if len(potentials_dict[i]) == 1:
            sing_lst.append(i)
    return sing_lst

