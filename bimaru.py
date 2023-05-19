# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 44:
# 102908 Luana Ferraz
# 103555 Ricardo Pereira 

import sys
import numpy as np
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe
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
    
    # !!! qnd fazemos tipo adicionar um b temos que no lines_capacity e cols_capacity atualizar
    # ja esta feito mas se encontrares algum sitio que falte mete pls
    def fill_top(self, row, col):
        if(col==0):
            self.board.representation[row, col+1] = "w"
            if(row!=0):
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
            if(row==8):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "b"
                self.board.update_capacities(row+1, col)
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
                self.board.representation[row+1, col] = "b"
                self.board.update_capacities(row+1, col)
            else:
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+2, col-1] = "w"
        else:
            self.board.representation[row, col-1] = "w"
            self.board.representation[row, col+1] = "w"
            self.board.representation[row-1, col+1] = "w"
            self.board.representation[row-1, col] = "w"
            self.board.representation[row-1, col-1] = "w"
            if(row==8):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "b"
                self.board.update_capacities(row+1, col)
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
                self.board.representation[row-1, col] = "t"
                self.board.update_capacities(row-1, col)
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
                self.board.representation[row-1, col] = "t"
                self.board.update_capacities(row-1, col)
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
                self.board.representation[row-1, col] = "t"
                self.board.update_capacities(row-1, col)
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
            self.board.representation[row, col-1] = "l"
            self.board.update_capacities(row, col-1)

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
            self.board.representation[row, col+1] = "r"
            self.board.update_capacities(row, col+1)

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
                self.board.representation[row-1, col-1] = "w"
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
                self.board.representation[row-1, col+1] = "w"
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
                    if col != 1:
                        self.board.representation[row+1, col+2] = "w"
                        self.board.representation[row-1, col+2] = "w"
                    if col != 8:
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

    def add_boat_4(self, pos_init: list, pos_end: list):
        pass
    def add_boat_3(self, pos_init: list, pos_end: list):
        pass
    def add_boat_2(self, pos_init: list, pos_end: list):
            
        self.board.representation[pos_init[0], pos_end[0]] = "c"
        pass
    def add_boat_1(self, pos_init: list):
        self.board.representation[pos_init[0], pos_init[1]] = "c"
        self.fill_around(pos_init[0], pos_init[1])
        pass

class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    def __init__(self, lines, cols, lines_capacity, cols_capacity, hints, representation):
        self.representation = representation
        self.lines = lines
        self.cols = cols
        self.lines_capacity = lines_capacity
        self.cols_capacity = cols_capacity     
        self.hints = hints

    def update_capacities(self, row: int, col: int):
        self.lines_capacity[row]-= 1
        self.cols_capacity[col]-= 1

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO
        return self.representation[(row, col)]

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        # TODO
        if (row == 0):
            return ("", self.representation[(row+1,col)])
        elif (row >= 9):
            return (self.representation[(row-1,col)], "")
        return(self.representation[(row-1, col)], self.representation[(row+1,col)])

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        if (col == 0):
            return ("", self.representation[(row,col+1)])
        elif (col >= 9):
            return (self.representation[(row,col-1)], "")
        return(self.representation[(row, col-1)], self.representation[(row,col+1)])

    def adjacent_diagonal_updown_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores na diagonal de cima para baixo da esquerda para a direita,
        respectivamente."""
        # TODO
        if ((col == 0) and (row < 9)) or ((row == 0) and (col < 9)): #n verifica se a linha ou coluna é u  valor negativo ou maior que 9, precisamos dessa verificação?
            return ("", self.representation[(row+1,col+1)])
        elif ((col == 9) and (row > 0)) or ((row == 9) and (col > 0)):
            return (self.representation[(row-1,col-1)], "")
        elif (((col==9) and (row == 0)) or ((col == 0) and (row == 9))):
            return ("","")
        return(self.representation[(row-1, col-1)], self.representation[(row+1,col+1)])

    def adjacent_diagonal_downup_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores na diagonal de baixo para cima, da esquerda para a direita,
        respectivamente."""
        # TODO
        if ((col == 0) and (row > 0)) or ((row == 9) and (col < 9)): #n verifica se a linha ou coluna é u  valor negativo ou maior que 9, precisamos dessa verificação?
            return ("", self.representation[(row-1,col+1)])
        elif ((col == 9) and (row < 9)) or ((row == 0) and (col > 0)):
            return (self.representation[(row+1,col-1)], "")
        elif (((col==9) and (row == 9)) or ((col == 0) and (row == 0))):
            return ("","")
        return(self.representation[(row+1, col-1)], self.representation[(row-1,col+1)])

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """
        # TODO
        from sys import stdin
        lines = [int(x) for x in stdin.readline().split()[1:]]
        cols = [int(x) for x in stdin.readline().split()[1:]]
        lines_capacity = lines.copy()
        cols_capacity = cols.copy()
        hints = []
        n_hints = int(stdin.readline())
        representation = np.chararray((10,10), unicode=True)
        representation[:] = "_"
        for _ in range(n_hints):
            lista = stdin.readline().split()
            hints.append(lista)
            representation[(int(lista[1]), int(lista[2]))] = lista[3]
            if(lista[3] != "W"):
                lines_capacity[int(lista[1])]-=1
                cols_capacity[int(lista[2])]-=1
        
        new_board = Board(lines, cols, lines_capacity, cols_capacity, hints, representation)
        return new_board



    # TODO: outros metodos da classe


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        #self.initial = board
        self.initial = BimaruState(board)
        # TODO
        pass

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""

        # TODO
        lista = []
        for i in range(len(state.board.lines_capacity)):
            if (state.board.lines_capacity[i] == 0):
               lista.append(["fill lines", i])
               state.board.lines_capacity[i] = -1
        for i in range(len(state.board.cols_capacity)):
            if (state.board.cols_capacity[i] == 0):
               lista.append(["fill cols", i])
               state.board.cols_capacity[i] = -1
        for i in range(len(state.board.hints)-1, -1, -1):
            if state.board.hints[i][3] == "T":
                lista.append(["fill top", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
            elif state.board.hints[i][3] == "B":
                lista.append(["fill bottom", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
            elif state.board.hints[i][3] == "R":
                lista.append(["fill right", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
            elif state.board.hints[i][3] == "L":
                lista.append(["fill left", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
            elif state.board.hints[i][3] == "C":
                lista.append(["fill around", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
                state.board.hints.pop(i)
            elif state.board.hints[i][3] == "M":
                lista.append(["fill middle", int(state.board.hints[i][1]), int(state.board.hints[i][2])])
        print(state.board.lines_capacity)
        return lista

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        if (action[0] == "fill lines"):
            state.fill_row(action[1])
        elif (action[0] == "fill cols"):
            state.fill_col(action[1])
        elif (action[0] == "fill top"):
            state.fill_top(action[1], action[2])
        elif (action[0] == "fill bottom"):
            state.fill_bottom(action[1], action[2])
        elif (action[0]=="fill around"):
            state.fill_around(action[1], action[2])
        elif (action[0]=="fill left"):
            state.fill_left(action[1], action[2])
        elif (action[0]=="fill right"):
            state.fill_right(action[1], action[2])
        elif (action[0] == "fill middle"):
            state.fill_middle(action[1], action[2])
        return state

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        """
        Todo preenchido #
        Todas as capacidades #
        Todos os barcos postos
        (n ha barcos colados)
        """
        # TODO
        if (state.board.representation[9,6] == "w"):
            return True
        if np.any(state.board.representation == "_"):
            return False
        for i in state.board.lines_capacity:
            if i not in (-1, 0):
                return False
        for i in state.board.cols_capacity:
            if i not in (-1, 0):
                return False
        boats = [1,1,1,1,2,2,2,3,3,4]
        for line in range(10):
            for col in range(10):
                value = state.board.representation[line]
                if value == "C" or value == "c":
                    if 1 in boats:
                        boats.remove(1)
                elif value == "T" or value == "t":
                    tamanho = 0
                    inc = 1
                    while state.board.representation[line, col + inc] != "b"\
                          or state.board.representation[line, col + inc] != "B":
                        if col + inc < 10:
                            inc += 1
                        else:
                            return False
                        tamanho += 1
                    if tamanho + 2 not in boats:
                        return False
                    else:
                        boats.remove(tamanho+2)


        return False

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    """board = Board()
    board.parse_instance(board)
    problem = Bimaru(board)
    initial_state = BimaruState(board)

    print(board.representation)
    print("\n")
    print(board.adjacent_vertical_values(10, 5))
    print("\n")"""

    board = Board.parse_instance()

    problem = Bimaru(board)
    
    #initial_state = BimaruState(board)
    
    #print(board.representation)
    
    #action = problem.actions(initial_state)
    #result_state = problem.result(initial_state, action)

    goal_node = depth_first_tree_search(problem)
    print("Solution:\n", goal_node.state.board.representation, sep="")

    # Mostrar valor na posição (3, 3):


    
    pass
