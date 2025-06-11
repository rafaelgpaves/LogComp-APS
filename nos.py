from symbol_table import SymbolTable
from tokens import *
import matplotlib.pyplot as plt
from matplotlib import image

def lower_bool(string):
    return str(string).lower()

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children: list = children

    def Evaluate(self, st):
        pass

class NoOp(Node):
    def Evaluate(self, st):
        return 
    
class IntVal(Node):
    def Evaluate(self, st):
        return (INT, self.value, False)
    
class BoolVal(Node):
    def Evaluate(self, st):
        return (BOOL, self.value, False)
    
class StrVal(Node):
    def Evaluate(self, st):
        return (STR, self.value, False)
    
class VarDec(Node):
    def Evaluate(self, st):
        st.create(self.children[0].value, self.value)
        if len(self.children) == 2:
            tipo, valor, _ = self.children[1].Evaluate(st)
            st.setter(self.children[0].value, (tipo, valor, False))

class Virar(Node):
    def Evaluate(self, st):
        coord = self.children[0].Evaluate(st)[1]
        x = st.getter("curr_x")[1]
        y = st.getter("curr_y")[1]
        dir = st.getter("curr_dir")[1]
        if dir == "x-pos":
            x_new = x + coord
            y_new = y
            if self.value == "direita":
                st.setter("curr_dir", ("string", "y-pos", False))
            elif self.value == "esquerda":
                st.setter("curr_dir", ("string", "y-neg", False))
        elif dir == "y-pos":
            x_new = x
            y_new = y + coord
            if self.value == "direita":
                st.setter("curr_dir", ("string", "x-neg", False))
            elif self.value == "esquerda":
                st.setter("curr_dir", ("string", "x-pos", False))
        elif dir == "x-neg":
            x_new = x - coord
            y_new = y
            if self.value == "direita":
                st.setter("curr_dir", ("string", "y-neg", False))
            elif self.value == "esquerda":
                st.setter("curr_dir", ("string", "y-pos", False))
        elif dir == "y-neg":
            x_new = x
            y_new = y - coord
            if self.value == "direita":
                st.setter("curr_dir", ("string", "x-pos", False))
            elif self.value == "esquerda":
                st.setter("curr_dir", ("string", "x-neg", False))
        X = [x, x_new]
        Y = [y, y_new]
        st.setter("curr_x", ("int", x_new, False))
        st.setter("curr_y", ("int", y_new, False))
        plt.plot(X, Y, color="black", linewidth=5)

class Continuar(Node):
    def Evaluate(self, st):
        coord = self.children[0].Evaluate(st)[1]
        x = st.getter("curr_x")[1]
        y = st.getter("curr_y")[1]
        dir = st.getter("curr_dir")[1]
        if dir == "x-pos":
            x_new = x + coord
            y_new = y
        elif dir == "y-pos":
            x_new = x
            y_new = y + coord
        elif dir == "x-neg":
            x_new = x - coord
            y_new = y
        elif dir == "y-neg":
            x_new = x
            y_new = y - coord
        X = [x, x_new]
        Y = [y, y_new]
        st.setter("curr_x", ("int", x_new, False))
        st.setter("curr_y", ("int", y_new, False))
        plt.plot(X, Y, color="black", linewidth=5)

class RuaDec(Node):
    def Evaluate(self, st):
        nome_rua = self.children[0].Evaluate(st)[1]
        
        try:
            if self.value == FECHADA:
                st.setter(nome_rua, ("int", 0, True))
            else:
                st.setter(nome_rua, ("int", 0, False))
        except:
            st.create(nome_rua, "int")
            if self.value == FECHADA:
                st.setter(nome_rua, ("int", 0, True))
            else:
                st.setter(nome_rua, ("int", 0, False))

class Se(Node):
    def Evaluate(self, st):
        if isinstance(self.children[0], StrVal):
            rua = self.children[0].Evaluate(st)[1]
            estado_rua = st.getter(rua)[2]
            estado_comparacao = self.value == FECHADA
            if estado_rua == estado_comparacao:
                self.children[1].Evaluate(st)
        else:
            posicao = self.children[0].Evaluate(st)[1]
            x = st.getter("curr_x")[1]
            y = st.getter("curr_y")[1]
            dir = st.getter("curr_dir")[1]
            if dir == "x-pos" or dir == "x-neg":
                if self.value == MAIOR:
                    estado_comparacao = x > posicao
                else:
                    estado_comparacao = x < posicao
            elif dir == "y-pos" or dir == "y-neg":
                if self.value == MAIOR:
                    estado_comparacao = y > posicao
                else:
                    estado_comparacao = y < posicao
            if estado_comparacao:
                self.children[1].Evaluate(st)
            

class Enquanto(Node):
    def Evaluate(self, st):
        if isinstance(self.children[0], StrVal):
            estado_comparacao = self.value == FECHADA
            while st.getter(self.children[0].Evaluate(st)[1])[2] == estado_comparacao:
                self.children[1].Evaluate(st)
        else:
            posicao = self.children[0].Evaluate(st)[1]
            x = st.getter("curr_x")[1]
            y = st.getter("curr_y")[1]
            dir = st.getter("curr_dir")[1]
            if dir == "x-pos" or dir == "x-neg":
                if self.value == MAIOR:
                    estado_comparacao = x > posicao
                else:
                    estado_comparacao = x < posicao
            elif dir == "y-pos" or dir == "y-neg":
                if self.value == MAIOR:
                    estado_comparacao = y > posicao
                else:
                    estado_comparacao = y < posicao
            while estado_comparacao:
                self.children[1].Evaluate(st)
                posicao = self.children[0].Evaluate(st)[1]
                x = st.getter("curr_x")[1]
                y = st.getter("curr_y")[1]
                dir = st.getter("curr_dir")[1]
                if dir == "x-pos" or dir == "x-neg":
                    if self.value == MAIOR:
                        estado_comparacao = x > posicao
                    else:
                        estado_comparacao = x < posicao
                elif dir == "y-pos" or dir == "y-neg":
                    if self.value == MAIOR:
                        estado_comparacao = y > posicao
                    else:
                        estado_comparacao = y < posicao
                


class Identifier(Node):
    def Evaluate(self, st):
        return st.getter(self.value)

class Assignment(Node):
    def Evaluate(self, st):
        tipo, valor, _ = self.children[1].Evaluate(st)
        st.setter(self.children[0].value, (tipo, valor, False))

class Block(Node):
    def Evaluate(self, st):
        new_st = SymbolTable()
        new_st.parent_st = st
        for child in self.children:
            if type(child) is Block:
                newer_st = SymbolTable()
                newer_st.parent_st = new_st
                result = child.Evaluate(newer_st)
            else:
                result = child.Evaluate(new_st)
        return None
