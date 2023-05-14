# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

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
    def fill_top(self, row, col):
        if(col==0):
            self.board.representation[row, col+1] = "w"
            if(row!=0):
                self.board.representation[row-1, col+1] = "w"
                self.board.representation[row-1, col] = "w"
            if(row==8):
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+1, col] = "b"
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
                self.board.representation[row+1, col-1] = "w"
            else:
                self.board.representation[row+1, col+1] = "w"
                self.board.representation[row+2, col+1] = "w"
                self.board.representation[row+1, col-1] = "w"
                self.board.representation[row+2, col-1] = "w"
        pass

        
        
    def fill_bottom(self, row, col):
        pass
    def fill_right(self, row, col):
        pass
    def fill_left(self, row, col):
        pass
    def add_boat_4(self, pos_init: list, direction: str):
        pass
    def add_boat_3(self, pos_init: list, direction: str):
        pass
    def add_boat_2(self, pos_init: list, direction: str):
        pass
    def add_boat_1(self, pos_init: list):
        pass

class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    def __init__(self):
        self.representation = np.chararray((10,10), unicode=True)
        self.representation[:] = "_"
        self.lines = []
        self.cols = []
        self.lines_capacity = []
        self.cols_capacity = []       
        self.hints = []



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
    def parse_instance(self):
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """
        # TODO
        from sys import stdin
        self.lines = [int(x) for x in stdin.readline().split()[1:]]
        self.cols = [int(x) for x in stdin.readline().split()[1:]]
        self.lines_capacity = self.lines.copy()
        self.cols_capacity = self.cols.copy()
        n_hints = int(stdin.readline())
        for _ in range(n_hints):
            lista = stdin.readline().split()
            self.hints.append(lista)
            self.representation[(int(lista[1]), int(lista[2]))] = lista[3]
            if(lista[3] != "W"):
                self.lines_capacity[int(lista[1])]-=1
                self.cols_capacity[int(lista[2])]-=1
        pass



    # TODO: outros metodos da classe


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = board
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
        for i in range(len(state.board.cols_capacity)):
            if (state.board.cols_capacity[i] == 0):
               lista.append(["fill cols", i])
        for hint in state.board.hints:
            if hint[3] == "T":
                lista.append(["fill top", int(hint[1]), int(hint[2])])
            elif hint[3] == "B":
                lista.append(["fill bottom", hint[1], hint[2]])
            elif hint[3] == "R":
                lista.append(["fill right", hint[1], hint[2]])
            elif hint[3] == "L":
                lista.append(["fill left", hint[1], hint[2]])
        return lista

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        for i in range(len(action)):
            if (action[i][0] == "fill lines"):
                state.fill_row(action[i][1])
            elif (action[i][0] == "fill cols"):
                state.fill_col(action[i][1])
            elif (action[i][0] == "fill top"):
                state.fill_top(action[i][1], action[i][2])
        pass

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

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

    board = Board()
    board.parse_instance(board)
    # Imprimir valores adjacentes

    # Criar uma instância de Bimaru:
    problem = Bimaru(board)
    # Criar um estado com a configuração inicial:
    initial_state = BimaruState(board)
    # Mostrar valor na posição (3, 3):
    print(board.representation)
    action = problem.actions(initial_state)
    # Realizar acção de inserir o valor w (água) na posição da linha 3 e coluna 3
    result_state = problem.result(initial_state, action)
    # Mostrar valor na posição (3, 3):
    print("\n")
    print(board.representation)


    
    pass
