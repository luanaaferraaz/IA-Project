# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 44:
# 102908 Luana Ferraz
# 103555 Ricardo Pereira
import sys
import numpy as np
import copy
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
    iterative_deepening_search,
)


class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    def fill_row(self, row: int):
        for i in range(10):
            if self.board.representation[(row, i)] == "_":
                self.board.representation[(row, i)] = "w"
        pass

    def fill_col(self, col: int):
        for i in range(10):
            if(self.board.representation[(i, col)] == "_"):
                self.board.representation[(i, col)] = "w"
        pass
 
    def fill_top(self, row, col):
        if(col==0):
            self.board.representation[row, col+1] = "w"
            if(row!=0):
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
            if(row==8):
                self.board.representation[row+1, col+1] = "w"
            else:
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+2, col+1] = "w"
        elif(col==9):
            self.board.representation[row, col-1] = "w"
            if(row!=0):
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col] = "w"
            if(row==8):
                self.board.representation[row+1, col-1] = "w"
            else:
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+2, col-1] = "w"
        else:
            self.board.representation[row, col-1] = "w"
            self.board.representation[row, col+1] = "w"
            if(row!=0):
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"
            if(row==8):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col-1] = "w"
            else:
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+2, col+1] = "w"
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+2, col-1] = "w"
        pass      
        
    def fill_bottom(self, row, col):
        if(col==0):
            self.board.representation[row, col+1] = "w"
            if(row!=9):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "w"
            if(row==1):
                self.board.representation[row-1, col+1] = "w"

            else:
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-2, col+1] = "w"
        elif(col==9):
            self.board.representation[row, col-1] = "w"
            if(row!=9):
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col] = "w"
            if(row==1):
                self.board.representation[row-1, col-1] = "w"
            else:
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-2, col-1] = "w"
        else:
            self.board.representation[row, col-1] = "w"
            self.board.representation[row, col+1] = "w"
            if(row!=9):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col-1] = "w"
            if(row==1):
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col-1] = "w"
            else:
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-2, col+1] = "w"
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-2, col-1] = "w"
        pass

    def fill_right(self, row, col):
        if col == 9:
            if row != 9:
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col-2] = "w"
            if row != 0:
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col-2] = "w"
        elif col == 1:
            if row != 0:
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col-1] = "w"
            if row != 9:
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
            self.board.representation[row, col+1] = "w"

        else:
            if row != 0:
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-2] = "w"
                self.board.representation[row-1, col+1] = "w"
            if row != 9:
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col-2] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
            self.board.representation[row, col+1] = "w"
        
                
        pass
    
    def fill_left(self, row, col):
        if (col == 0):
            if (row!=0):
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col+2] = "w"
            if (row!=9):
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col+2] = "w"                
        elif (col == 8):
            if (row != 9):
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
            if (row != 0):
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
            self.board.representation[row, col-1] = "w"

        else:
            if (row != 9):
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col+2] = "w"
            if ( row != 0):
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col+2] = "w"
            self.board.representation[row, col-1] = "w"
        pass
    
    def fill_around(self, row, col):
        if(col==0):
            if(row==0):
                self.board.representation[row+1, col] = "w"
                self.board.representation[row, col+1] = "w"
                self.board.representation[row+1, col+1] = "w"
            elif(row==9):
                self.board.representation[row, col+1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
            else:
                self.board.representation[row, col+1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col+1] = "w"
        elif(col==9):
            if(row==0):
                self.board.representation[row+1, col] = "w"
                self.board.representation[row, col-1] = "w"
                self.board.representation[row+1, col-1] = "w"
            elif(row==9):
                self.board.representation[row, col-1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"
            else:
                self.board.representation[row, col-1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"
        else:
            self.board.representation[row, col-1] = "w"
            self.board.representation[row, col+1] = "w"
            if(row!=9):
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+1, col+1] = "w"
            if(row!=0):    
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"
                self.board.representation[row-1, col+1] = "w"

    def fill_row_line(self, row, col, row_end, col_end, size):
        if(row==row_end):
            i=0
            while(i<size):
                if(self.board.cols_capacity[col+i]<=0): self.fill_col(col+i)
                i+=1
            if(self.board.lines_capacity[row]<=0): self.fill_row(row)

        # mesma coluna
        elif(col==col_end):
            i=0
            while(i<size):
                if(self.board.lines_capacity[row+i]<=0): self.fill_row(row+i)
                i+=1
            if(self.board.cols_capacity[col]<=0): self.fill_col(col)

    def fill_middle(self, row, col):
        if col == 0:
            if row != 1:
                self.board.representation[row-2, col+1] = "w"
            if row != 8:
                self.board.representation[row+2, col+1] = "w"
            self.board.representation[row-1, col+1] = "w"
            self.board.representation[row, col+1] = "w"
            self.board.representation[row+1, col+1] = "w"
        elif col == 9:
            if row != 1:
                self.board.representation[row-2, col-1] = "w"
            if row != 8:
                self.board.representation[row+2, col-1] = "w"
            self.board.representation[row-1, col-1] = "w"
            self.board.representation[row, col-1] = "w"
            self.board.representation[row+1, col-1] = "w"
        else:
            if row == 0:
                if col != 1:
                    self.board.representation[row+1, col-2] = "w"
                if col != 8:
                    self.board.representation[row+1, col+2] = "w"
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "w"
                self.board.representation[row+1, col-1] = "w"  
            elif row == 9:
                if col != 1:
                    self.board.representation[row-1, col-2] = "w"
                if col != 8:
                    self.board.representation[row-1, col+2] = "w"
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
                self.board.representation[row-1, col-1] = "w"  
            else:
                verticals = self.board.adjacent_vertical_values(row, col)
                horizontals = self.board.adjacent_horizontal_values(row, col)
                if "w" in verticals or "W" in verticals or \
                      "M" in horizontals or "m" in horizontals:
                    if col != 8:
                        self.board.representation[row+1, col+2] = "w"
                        self.board.representation[row-1, col+2] = "w"
                    if col != 1:
                        self.board.representation[row+1, col-2] = "w"
                        self.board.representation[row-1, col-2] = "w"
                    self.board.representation[row+1, col+1] = "w"
                    self.board.representation[row+1, col] = "w"
                    self.board.representation[row+1, col-1] = "w" 
                    self.board.representation[row-1, col+1] = "w"
                    self.board.representation[row-1, col] = "w"
                    self.board.representation[row-1, col-1] = "w"
                elif "w" in horizontals or "W" in horizontals or \
                    "M" in verticals or "m" in verticals:
                    if row != 1:
                        self.board.representation[row-2, col+1] = "w"
                        self.board.representation[row-2, col-1] = "w"
                    if row != 8:
                        self.board.representation[row+2, col+1] = "w"
                        self.board.representation[row+2, col-1] = "w"
                    self.board.representation[row+1, col+1] = "w"
                    self.board.representation[row, col+1] = "w"
                    self.board.representation[row-1, col+1] = "w" 
                    self.board.representation[row+1, col-1] = "w"
                    self.board.representation[row, col-1] = "w"
                    self.board.representation[row-1, col-1] = "w"

    def is_free_around(self, row, col):
        (up, down) = self.board.adjacent_vertical_values(row, col)
        if(up not in ("W", "w", "", "_") or down not in ("W", "w", "", "_")):
            return False
        (left, right) = self.board.adjacent_horizontal_values(row, col)
        if(left not in ("W", "w", "", "_") or right not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_updown_values(row, col)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_downup_values(row, col)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        return True

    def is_free_vertical(self, row_i, col_i, row_e, col_e):
        (up, down) = self.board.adjacent_vertical_values(row_i, col_i)
        if(up not in ("W", "w", "", "_")):
            return False
        (left, right) = self.board.adjacent_horizontal_values(row_i, col_i)
        if(left not in ("W", "w", "", "_") or right not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_updown_values(row_i, col_i)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_downup_values(row_i, col_i)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        
        (up, down) = self.board.adjacent_vertical_values(row_e, col_e)
        if(down not in ("W", "w", "", "_")):
            return False
        (left, right) = self.board.adjacent_horizontal_values(row_e, col_e)
        if(left not in ("W", "w", "", "_") or right not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_updown_values(row_e, col_e)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_downup_values(row_e, col_e)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        return True
    
    def is_free_horizontal(self, row_i, col_i, row_e, col_e):
        (up, down) = self.board.adjacent_vertical_values(row_i, col_i)
        if(up not in ("W", "w", "", "_") or down not in ("W", "w", "", "_")):
            return False
        (left, right) = self.board.adjacent_horizontal_values(row_i, col_i)
        if(left not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_updown_values(row_i, col_i)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_downup_values(row_i, col_i)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        
        (up, down) = self.board.adjacent_vertical_values(row_e, col_e)
        if(up not in ("W", "w", "", "_") or down not in ("W", "w", "", "_")):
            return False
        (left, right) = self.board.adjacent_horizontal_values(row_e, col_e)
        if(right not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_updown_values(row_e, col_e)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        (diag1, diag2) = self.board.adjacent_diagonal_downup_values(row_e, col_e)
        if(diag1 not in ("W", "w", "", "_") or diag2 not in ("W", "w", "", "_")):
            return False
        return True

    def check_boat_1(self):
        boats_to_add = []
        for l in range(10):
            if(self.board.lines_capacity[l]>=1):
                for col in range(10):
                    
                    if(self.board.cols_capacity[col]<1):
                        continue
                    value = self.board.get_value(l, col)
                    if(value== "_"):
                        if(self.is_free_around(l, col)):
                            boats_to_add += [["one", [l, col]]]

        return boats_to_add

    def check_boats2(self):
        boats_to_add = []
        start_row = 0
        if(self.board.last_two[0][0]!=-1):
            start_row = self.board.last_two[0][0]
        for row in range(start_row, 10):
            for col in range(10):
                value=self.board.get_value(row, col)
                count2=0
                if(value in ["L","_"] and self.board.cols_capacity[col]>=1):
                    if(self.board.lines_capacity[row]>=2 and col < 9 and self.board.get_value(row, col+1) in ["R", "_"]):
                        if(self.board.cols_capacity[col+1]>=1):
                            count2=2

                        if(count2==2):
                            if(self.is_free_horizontal(row, col, row, col+1)):
                                boats_to_add += [["two", [row, col], [row, col+1]]]
                    
                count2=0
                if(value in ["T", "_"] and self.board.lines_capacity[row]>=1):
                    if(self.board.cols_capacity[col]>=2 and row < 9 and self.board.get_value(row+1, col) in ["B", "_"]):
                        if(self.board.lines_capacity[row+1]>=1):
                            count2=2

                        if(count2==2):
                            if(self.is_free_vertical(row, col, row+1, col)):
                                boats_to_add += [["two", [row, col], [row+1, col]]]      
        return boats_to_add


    def check_boats3(self):
        boats_to_add = []
        start_row = 0
        if(self.board.last_three[0][0]!=-1):
            start_row = self.board.last_three[0][0]
        for row in range(start_row, 10):            
            for col in range(10):
                value=self.board.get_value(row, col)
                if(value in ["L","_"] and self.board.cols_capacity[col]>=1):
                    count3 = 1
                    if(self.board.lines_capacity[row]>=3 and col < 8 and self.board.get_value(row, col+2) in ["R", "_"]):
                        if(self.board.cols_capacity[col+2]>=1):count3+=1
                        if(self.board.cols_capacity[col+1]>=1): 
                            value=self.board.get_value(row, col+1)
                            if(value=="_" or value=="M"): 
                                count3 += 1
                    
                   
                        if(count3==3):
                            if(self.is_free_horizontal(row, col, row, col+2)):
                                boats_to_add += [["three", [row, col], [row, col+2]]]
                    
                if(value in ["T", "_"] and self.board.lines_capacity[row]>=1):
                    count3 = 1
                    if(self.board.cols_capacity[col]>=3 and row < 8 and self.board.get_value(row+2, col) in ["B", "_"]):
                        if(self.board.lines_capacity[row+2]>=1):count3+=1
                        if(self.board.lines_capacity[row+1]>=1): 
                            value=self.board.get_value(row+1, col)
                            if(value=="_" or value=="M"): 
                                count3 += 1
                   
                        if(count3==3):
                            if(self.is_free_vertical(row, col, row+2, col)):
                                boats_to_add += [["three", [row, col], [row+2, col]]]   
        return boats_to_add

    def check_boats4(self):
        boats_to_add = []
        for row in range(10):
            for col in range(10):
                value=self.board.get_value(row, col)
                if(value in ["L","_"] and self.board.cols_capacity[col]>=1):
                    count4 = 1
                    if(self.board.lines_capacity[row]>=4 and col < 7 and self.board.get_value(row, col+3) in ["R","_"]):  
                        if(self.board.cols_capacity[col+3]>=1):count4+=1
                        for i in range(1,3):
                            if(self.board.cols_capacity[col+i]<1):
                                break
                            value=self.board.get_value(row, col+i)
                            if(value=="_" or value=="M"): 
                                count4 += 1


                        if(count4==4):
                                if(self.is_free_horizontal(row, col, row, col+3)):
                                    boats_to_add += [["four", [row, col], [row, col+3]]]
                        
                    
                if(value in ["T", "_"] and self.board.lines_capacity[row]>=1):
                    count4 = 1
                    if(self.board.cols_capacity[col]>=4 and row < 7 and self.board.get_value(row+3, col) in ["B","_"]):
                        if(self.board.lines_capacity[row+3]>=1):
                            count4+=1
                        for i in range(1,3):
                            if(self.board.lines_capacity[row+i]<1):
                                break
                            value=self.board.get_value(row+i, col)
                            if(value=="_" or value=="M"): 
                                count4 += 1


                        if(count4==4):
                                if(self.is_free_vertical(row, col, row+3, col)):
                                    boats_to_add += [["four", [row, col], [row+3, col]]]    
        return boats_to_add 

    def add_boat_4(self, pos_init: list, pos_end: list):
        # mesma linha
        if(pos_init[0]-pos_end[0] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "l"
            self.board.update_capacities(pos_init[0], pos_init[1])
            for i in range(1,3):
                self.board.representation[pos_init[0], pos_init[1]+i] = "m"
                self.board.update_capacities(pos_init[0], pos_init[1]+i)
            self.board.representation[pos_end[0], pos_end[1]] = "r"
            self.board.update_capacities(pos_end[0], pos_end[1])
            self.fill_left(pos_init[0], pos_init[1])
            self.fill_right(pos_end[0], pos_end[1])            

        # mesma coluna
        elif(pos_init[1]-pos_end[1] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "t"
            self.board.update_capacities(pos_init[0], pos_init[1])
            for i in range(1,3):
                self.board.representation[pos_init[0]+i, pos_init[1]] = "m"
                self.board.update_capacities(pos_init[0]+i, pos_init[1])
            self.board.representation[pos_end[0], pos_end[1]] = "b"
            self.board.update_capacities(pos_end[0], pos_end[1])
            self.fill_top(pos_init[0], pos_init[1])
            self.fill_bottom(pos_end[0], pos_end[1])          
        self.board.boats_left4-=1

        pass
    
    def add_boat_3(self, pos_init: list, pos_end: list):
        if(pos_init[0]-pos_end[0] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "l"
            self.board.update_capacities(pos_init[0], pos_init[1])
            self.board.representation[pos_init[0], pos_init[1]+1] = "m"
            self.board.update_capacities(pos_init[0], pos_init[1]+1)
            self.board.representation[pos_end[0], pos_end[1]] = "r"
            self.board.update_capacities(pos_end[0], pos_end[1])
            self.fill_left(pos_init[0], pos_init[1])
            self.fill_right(pos_end[0], pos_end[1]) 


        # mesma coluna
        elif(pos_init[1]-pos_end[1] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "t"
            self.board.update_capacities(pos_init[0], pos_init[1])
            self.board.representation[pos_init[0]+1, pos_init[1]] = "m"
            self.board.update_capacities(pos_init[0]+1, pos_init[1])
            self.board.representation[pos_end[0], pos_end[1]] = "b"
            self.board.update_capacities(pos_end[0], pos_end[1])
            self.fill_top(pos_init[0], pos_init[1])
            self.fill_bottom(pos_end[0], pos_end[1]) 

        self.board.boats_left3-=1

        pass

    def add_boat_2(self, pos_init: list, pos_end: list):
            
        if(pos_init[0]-pos_end[0] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "l"
            self.board.update_capacities(pos_init[0], pos_init[1])
            
            self.board.representation[pos_init[0], pos_end[1]] = "r"
            self.board.update_capacities(pos_init[0], pos_end[1])
            self.fill_left(pos_init[0], pos_init[1])
            if(pos_end[1]<9 and self.board.get_value(pos_end[0], pos_end[1]+1)!= "W"):
                self.board.representation[pos_end[0], pos_end[1]+1]= "w"


        # mesma coluna
        elif(pos_init[1]-pos_end[1] == 0):
            self.board.representation[pos_init[0], pos_init[1]] = "t"
            self.board.update_capacities(pos_init[0], pos_init[1])
            
            self.board.representation[pos_end[0], pos_end[1]] = "b"
            self.board.update_capacities(pos_end[0], pos_end[1]) 
            self.fill_top(pos_init[0], pos_init[1])
            if(pos_end[0]<9 and self.board.get_value(pos_end[0]+1, pos_end[1])!= "W"):
                self.board.representation[pos_end[0]+1, pos_end[1]]= "w"
        self.board.boats_left2-=1

        pass

    def add_boat_1(self, pos_init: list):
        self.board.representation[pos_init[0], pos_init[1]] = "c"
        self.fill_around(pos_init[0], pos_init[1])
        self.board.boats_left1-=1
        self.board.update_capacities(pos_init[0], pos_init[1])
        pass

class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    def __init__(self, lines, cols, lines_capacity, cols_capacity, hints, representation, boats_left, copy_hints):
        self.representation = representation
        self.lines = lines
        self.cols = cols
        self.lines_capacity = lines_capacity
        self.cols_capacity = cols_capacity     
        self.hints = hints
        self.boats_left4 = 1
        self.boats_left3 = 2
        self.boats_left2 = 3
        self.boats_left1 = boats_left
        self.copy_hints = copy_hints
        self.last_two = ([-1,-1],[-1,-1])
        self.last_three = ([-1,-1],[-1,-1])

    def update_capacities(self, row: int, col: int):
        self.lines_capacity[row]-= 1
        self.cols_capacity[col]-= 1

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.representation[(row, col)]

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        if (row == 0):
            return ("", self.get_value(row+1,col))
        elif (row >= 9):
            return (self.get_value(row-1,col), "")
        return(self.get_value(row-1, col), self.get_value(row+1,col))

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        if (col == 0):
            return ("", self.get_value(row,col+1))
        elif (col >= 9):
            return (self.get_value(row,col-1), "")
        return(self.get_value(row, col-1), self.get_value(row,col+1))

    def adjacent_diagonal_updown_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores na diagonal de cima para baixo da esquerda para a direita,
        respectivamente."""
        if ((col == 0) and (row < 9)) or ((row == 0) and (col < 9)): 
            return ("", self.get_value(row+1,col+1))
        elif ((col == 9) and (row > 0)) or ((row == 9) and (col > 0)):
            return (self.get_value(row-1,col-1), "")
        elif (((col==9) and (row == 0)) or ((col == 0) and (row == 9))):
            return ("","")
        return(self.get_value(row-1, col-1), self.get_value(row+1,col+1))

    def adjacent_diagonal_downup_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores na diagonal de baixo para cima, da esquerda para a direita,
        respectivamente."""
        if ((col == 0) and (row > 0)) or ((row == 9) and (col < 9)): 
            return ("", self.get_value(row-1,col+1))
        elif ((col == 9) and (row < 9)) or ((row == 0) and (col > 0)):
            return (self.get_value(row+1,col-1), "")
        elif (((col==9) and (row == 9)) or ((col == 0) and (row == 0))):
            return ("","")
        return(self.get_value(row+1, col-1), self.get_value(row-1,col+1))
    
    def print_solution(self):
        for i in self.copy_hints:
            self.representation[int(i[1]), int(i[2])] = i[3]
        for line in range(10):
            for col in range(10):
                value = self.representation[line, col]
                if value == "w" or value=="_":
                    print(".", end="")
                else:
                    print(value, end="")
            print()

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """
        from sys import stdin
        lines = [int(x) for x in stdin.readline().split()[1:]]
        cols = [int(x) for x in stdin.readline().split()[1:]]
        lines_capacity = lines.copy()
        cols_capacity = cols.copy()
        hints = []
        boats_left1=4
        n_hints = int(stdin.readline())
        representation = np.chararray((10,10), unicode=True)
        representation[:] = "_"
        for _ in range(n_hints):
            lista = stdin.readline().split()
            hints.append(lista)
            representation[(int(lista[1]), int(lista[2]))] = lista[3]
            if(lista[3]=="C"):
                lines_capacity[int(lista[1])]-=1
                cols_capacity[int(lista[2])]-=1
                boats_left1-=1
        copy_hints = hints.copy()
        new_board = Board(lines, cols, lines_capacity, cols_capacity, hints, representation, boats_left1, copy_hints)
        
        for row in range(len(new_board.lines_capacity)):
            if (new_board.lines_capacity[row] == 0):
                new_board.lines_capacity[row] = -1
                for c in range(10):
                    if new_board.representation[(row, c)] == "_":
                        new_board.representation[(row, c)] = "w"
                
        for col in range(len(new_board.cols_capacity)):
            if (new_board.cols_capacity[col] == 0):
                new_board.cols_capacity[col] = -1
                for line in range(10):
                    if(new_board.representation[(line, col)] == "_"):
                        new_board.representation[(line, col)] = "w"        
        
        return new_board


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = BimaruState(board)
        pass

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        lista = []
        for i in range(len(state.board.hints)-1, -1, -1):

            if state.board.hints[i][3] == "T":
                lista.append(["fill top", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
            elif state.board.hints[i][3] == "B":
                lista.append(["fill bottom", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
            elif state.board.hints[i][3] == "R":
                lista.append(["fill right", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
            elif state.board.hints[i][3] == "L":
                lista.append(["fill left", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
            elif state.board.hints[i][3] == "C":
                lista.append(["fill around", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
            elif state.board.hints[i][3] == "M":
                lista.append(["fill middle", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
                return lista
    
        if(state.board.boats_left4!=0):
            lista+=state.check_boats4()
            return lista
        if(state.board.boats_left3!=0):
            lista+=state.check_boats3()
            return lista
        if(state.board.boats_left2!=0):
            lista+=state.check_boats2() 
            lista.reverse() 
            return lista
        if(state.board.boats_left1!=0):
            lista+=state.check_boat_1()
            return lista
        
        
        return lista

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        state_new = BimaruState(copy.deepcopy(state.board))
        
        if(action[0] == "four" and state_new.board.boats_left4!=0):
            state_new.add_boat_4(action[1], action[2])
            state_new.fill_row_line(action[1][0], action[1][1], action[2][0], action[2][1],4)
        elif(action[0] == "three" and state_new.board.boats_left3!=0):
            state_new.add_boat_3(action[1], action[2])  
            state_new.fill_row_line(action[1][0], action[1][1], action[2][0], action[2][1],3)
            state_new.board.last_three = (action[1], action[2])        
        elif(action[0] == "two" and state_new.board.boats_left2!=0):
            state_new.add_boat_2(action[1], action[2])
            state_new.fill_row_line(action[1][0], action[1][1], action[2][0], action[2][1],2)
            state_new.board.last_two = (action[1], action[2])
        elif(action[0] == "one" and state_new.board.boats_left1!=0):
            state_new.add_boat_1(action[1])
            state_new.fill_row_line(action[1][0], action[1][1], action[1][0], action[1][1],1)
        elif (action[0] == "fill lines"):
            state_new.fill_row(action[1])
        elif (action[0] == "fill cols"):
            state_new.fill_col(action[1])
        elif (action[0] == "fill top"):
            state_new.fill_top(action[1], action[2])
        elif (action[0] == "fill bottom"):
            state_new.fill_bottom(action[1], action[2])
        elif (action[0]=="fill around"):
            state_new.fill_around(action[1], action[2])
        elif (action[0]=="fill left"):
            state_new.fill_left(action[1], action[2])
        elif (action[0]=="fill right"):
            state_new.fill_right(action[1], action[2])
        elif (action[0] == "fill middle"):
            state_new.fill_middle(action[1], action[2]) 
         
        return state_new

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""

        if(state.board.boats_left1!=0 or state.board.boats_left2!=0 or state.board.boats_left3!=0 or state.board.boats_left4!=0):
            return False

        for i in state.board.lines_capacity:
            if i not in (-1, 0):         
                return False
        for i in state.board.cols_capacity:
            if i not in (-1, 0):
                return False
        
        for hint in state.board.copy_hints:
            if(hint[3]=="T" and state.board.get_value(int(hint[1])+1, int(hint[2])) not in ("b", "m")):
                return False
            if(hint[3]=="B" and state.board.get_value(int(hint[1])-1, int(hint[2])) not in ("t", "m")):
                return False
            if(hint[3]=="L" and state.board.get_value(int(hint[1]), int(hint[2])+1) not in ("r", "m")):
                return False
            if(hint[3]=="R" and state.board.get_value(int(hint[1]), int(hint[2])-1) not in ("l", "m")):
                return False
            if(hint[3]=="M"):
                left, right, top, bottom = "?", "?", "?", "?"
                if(int(hint[2])>0): left = state.board.get_value(int(hint[1]), int(hint[2])-1) 
                if(int(hint[2])<9): right = state.board.get_value(int(hint[1]), int(hint[2])+1)
                if(int(hint[1])>0): top = state.board.get_value(int(hint[1])-1, int(hint[2]))
                if(int(hint[1])<9):bottom = state.board.get_value(int(hint[1])+1, int(hint[2]))
                if(left not in ["l", "m", "?"] and right not in ["r", "m", "?"]):
                    if(bottom not in ("b", "m", "?") and top not in ("t", "m", "?")):
                        return False
        return True

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board = Board.parse_instance()

    problem = Bimaru(board)
    
    goal_node = depth_first_tree_search(problem)   

    goal_node.state.board.print_solution()
   
