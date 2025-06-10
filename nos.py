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

class FuncDec(Node):
    def Evaluate(self, st):
        st.create(self.children[0].value, self.value)
        st.setter(self.children[0].value, (self.value, self, True))

class FuncCall(Node):
    def Evaluate(self, st):
        func = st.getter(self.value)
        funcdec = func[1]
        if func[2] is False:
            raise Exception(f"\"{self.value}\" não é chamável")
        if len(self.children) != len(funcdec.children) - 2:
            raise Exception(f"Número de argumentos recebidos: {len(self.children)}; A função \"{self.value}\" esperava {len(funcdec.children) - 2} argumentos")
        new_st = SymbolTable()
        new_st.parent_st = st

        for i, arg in enumerate(self.children):
            tipo, valor, _ = arg.Evaluate(new_st)
            iden_arg = funcdec.children[i+1].children[0].value
            tipo_arg = funcdec.children[i+1].value
            new_st.create(iden_arg, tipo)
            new_st.setter(iden_arg, (tipo, valor, False))

        retorno_func = funcdec.children[-1].Evaluate(new_st)
        if isinstance(retorno_func, Retorno):
            retorno_func = retorno_func.value

        return_type = func[0]
        if retorno_func is None:
            if return_type != "":
                raise Exception(f"Retorno tipo None não esperada para uma função \"{self.value}\" tipo void")
        else:
            if return_type != retorno_func[0]:
                raise Exception(f"Retorno tipo {retorno_func[0]} não esperada para uma função \"{self.value}\" tipo {return_type}")
        return retorno_func

class Retorno:
    def __init__(self, value):
        self.value = value

class Return(Node):
    def Evaluate(self, st):
        result = self.children[0].Evaluate(st)
        return Retorno(result)

class UnOp(Node):
    def Evaluate(self, st):
        result = self.children[0].Evaluate(st)
        if self.value == MINUS:
            if result[0] == INT:
                return (INT, - result[1], False)
            raise Exception(f"Tipo esperado: INT; Tipo recebido: {result[0]}")
        if self.value == PLUS:
            if result[0] == INT:
                return (INT, result[1], False)
            raise Exception(f"Tipo esperado: INT; Tipo recebido: {result[0]}")
        if self.value == NOT:
            if result[0] == BOOL:
                return (BOOL, lower_bool(not BOOLEANS[result[1]]), False)
            raise Exception(f"Tipo esperado: BOOL; Tipo recebido: {result[0]}")

class BinOp(Node):
    def Evaluate(self, st):
        result0 = self.children[0].Evaluate(st)
        result1 = self.children[1].Evaluate(st)
        if self.value == MULT:
            if result0[0] == INT and result1[0] == INT:
                return (INT, result0[1] * result1[1], False)
            raise Exception(f"Tipos esperados: INT e INT; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == DIV:
            if result0[0] == INT and result1[0] == INT:
                return (INT, result0[1] // result1[1], False)
            raise Exception(f"Tipos esperados: INT e INT; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == MINUS:
            if result0[0] == INT and result1[0] == INT:
                return (INT, result0[1] - result1[1], False)
            raise Exception(f"Tipos esperados: INT e INT; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == PLUS:
            if result0[0] == INT and result1[0] == INT:
                return (INT, result0[1] + result1[1], False)
            str0 = result0[1]
            str1 = result1[1]
            if result0[0] == BOOL:
                str0 = str(result0[1]).lower()
            if result1[0] == BOOL:
                str1 = str(result1[1]).lower()
            return (STR, f"{str0}{str1}", False)
        if self.value == AND:
            if result0[0] == BOOL and result1[0] == BOOL:
                return (BOOL, lower_bool(BOOLEANS[result0[1]] and BOOLEANS[result1[1]]), False)
            raise Exception(f"Tipos esperados: BOOL e BOOL; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == OR:
            if result0[0] == BOOL and result1[0] == BOOL:
                return (BOOL, lower_bool(BOOLEANS[result0[1]] or BOOLEANS[result1[1]]), False)
            raise Exception(f"Tipos esperados: BOOL e BOOL; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == EQUAL:
            if result0[0] == INT and result1[0] == INT or result0[0] == BOOL and result1[0] == BOOL or result0[0] == STR and result1[0] == STR:
                return (BOOL, lower_bool(result0[1] == result1[1]), False)
            raise Exception(f"Tipos esperados: INT e INT ou BOOL e BOOL ou STR e STR; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == MORE:
            if result0[0] == INT and result1[0] == INT or result0[0] == STR and result1[0] == STR:
                return (BOOL, lower_bool(result0[1] > result1[1]), False)
            raise Exception(f"Tipos esperados: INT e INT ou STR e STR; Tipos recebidos: {result0[0]} e {result1[0]}")
        if self.value == LESS:
            if result0[0] == INT and result1[0] == INT or result0[0] == STR and result1[0] == STR:
                return (BOOL, lower_bool(result0[1] < result1[1]), False)
            raise Exception(f"Tipos esperados: INT e INT ou STR e STR; Tipos recebidos: {result0[0], result0[1]} e {result1[0], result1[1]}")

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
        rua = self.children[0].Evaluate(st)[1]
        estado_rua = st.getter(rua)[2]
        estado_comparacao = self.value == FECHADA
        if estado_rua == estado_comparacao:
            self.children[1].Evaluate(st)

class Enquanto(Node):
    def Evaluate(self, st):
        estado_comparacao = self.value == FECHADA
        while st.getter(self.children[0].Evaluate(st)[1])[2] == estado_comparacao:
            self.children[1].Evaluate(st)


class Identifier(Node):
    def Evaluate(self, st):
        return st.getter(self.value)
    
class Print(Node):
    def Evaluate(self, st):
        print(self.children[0].Evaluate(st)[1])

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
            if type(result) is Retorno:
                return result
        return None

class If(Node):
    def Evaluate(self, st):
        if self.children[0].Evaluate(st)[0] != BOOL:
            raise Exception(f"Condição para if (tipo BOOL) esperada; tipo recebido: {self.children[0].Evaluate(st)[0]}")
        if BOOLEANS[self.children[0].Evaluate(st)[1]]:
            result = self.children[1].Evaluate(st)
            if type(result) is Retorno:
                return result
        else:
            if len(self.children) == 3:
                result = self.children[2].Evaluate(st)
                if type(result) is Retorno:
                    return result

class While(Node):
    def Evaluate(self, st):
        if self.children[0].Evaluate(st)[0] != BOOL:
            raise Exception(f"Condição para for (tipo BOOL) esperada; tipo recebido: {self.children[0].Evaluate(st)[0]}")
        while BOOLEANS[self.children[0].Evaluate(st)[1]]:
            result = self.children[1].Evaluate(st)
            if type(result) is Retorno:
                return result

class Read(Node):
    def Evaluate(self, st):
        return (INT, int(input()), False)
