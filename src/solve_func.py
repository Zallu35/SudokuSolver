from Funcs import logic

def solve_puzzle(game_board, potentials_dict, boxes_dict): #this will be the function assigned to the solve button when all the logic is finished
    board_filled = False
    loops = 1
    unchanged_loops = 0
    while (board_filled == False) and (unchanged_loops < 3):
        print(f"loops: {loops}, unchanged: {unchanged_loops}") #used for debugging
        unchanged_loops += 1
        loops += 1
        print('fill') #used for debugging
        flag = logic.fill_singles(game_board, potentials_dict, boxes_dict)
        if flag > 0:
            unchanged_loops = 0
        print('rows') #used for debugging
        flag = logic.potentials_row_scan(game_board, potentials_dict, boxes_dict)
        if flag > 0:
            unchanged_loops = 0
            continue
        print('columns') #used for debugging
        flag = logic.potentials_column_scan(game_board, potentials_dict, boxes_dict)
        if flag > 0:
            unchanged_loops = 0
            continue
        print('boxes') #used for debugging
        flag = logic.potentials_box_scan(game_board, potentials_dict, boxes_dict)
        if flag > 0:
            unchanged_loops = 0
            continue
        total_empties = 0
        for row in game_board:
            total_empties += row.count(0)
        if total_empties == 0:
            board_filled = True
        print(f"total empty cells: {total_empties}") #used for debugging