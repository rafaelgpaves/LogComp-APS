import sys
import re

from nos import *
from symbol_table import SymbolTable
from tokens import *

class Token:
    def __init__(self, tipo: str):
        self.type: str = tipo
        self.value: int = 0

class PrePro:
    def filter(self, code: str):
        code = code.replace("\t", "")
        if re.search(r".*//.*\n", code):
            return re.sub("//.*\n", "\n", code)
        return code

class Tokenizer:

    def __init__(self, src: str):
        self.source: str = src
        self.position: int = 0
        self.next: Token

    def selectNext(self):
        if self.position == len(self.source):
            self.next = Token(EOF)
            return
        
        while self.source[self.position] == " ":
            self.position += 1
            if self.position == len(self.source):
                self.next = Token(EOF)
                return

        if self.source[self.position].isdigit():
            self.next = Token(INT)
            while self.source[self.position].isdigit():
                self.next.value = self.next.value*10 + int(self.source[self.position])
                self.position += 1

                if self.position == len(self.source):
                    return
                
            return

        if self.source[self.position].isalpha():
            self.next = Token(IDEN)
            self.next.value = ""
            while self.source[self.position].isalnum() or self.source[self.position] == "_":
                
                self.next.value += str(self.source[self.position])
                self.position += 1
                if self.next.value in KEYWORDS:
                    self.next = Token(KEYWORDS[self.next.value])
                    return
                
                if self.position == len(self.source):
                    return
                
            if self.next.value in KEYWORDS:
                self.next = Token(KEYWORDS[self.next.value])
                return
        
            return
        
        if self.source[self.position] == "\"":
            self.next = Token(STR)
            self.next.value = ""
            self.position += 1
            while True:
                if self.source[self.position] == "\"":
                    self.position += 1
                    return
                self.next.value += str(self.source[self.position])
                self.position += 1
                if self.position == len(self.source):
                    return

        if self.source[self.position] == "-":
            self.next = Token(OPTION)
            self.position += 1
            return
        elif self.source[self.position] == "\n":
            self.next = Token(NL)
            self.position += 1
            return
        elif self.source[self.position] == ",":
            self.next = Token(COMMA)
            self.position += 1
            return
        elif self.source[self.position] == ":":
            self.next = Token(COLON)
            self.position += 1
            return
        elif self.source[self.position] == ";":
            self.next = Token(SEMICOLON)
            self.position += 1
            return
        raise Exception(f"Letra \"{self.source[self.position]}\" não existente")

class Parser:

    def __init__(self):
        self.tokenizer: Tokenizer

    def parseProgram(self):
        bloco = Block("", [])
        token = self.tokenizer.next
        if token.type != PARTIDA:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COLON:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != RUA:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != IDEN:
            raise Exception("Token errado")
        no = VarDec("", [])
        no.children.append(Identifier(token.value, []))
        bloco.children.append(no)
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COMMA:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != INT:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != NL:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != DESTINO:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COLON:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != RUA:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != IDEN:
            raise Exception("Token errado")
        no = VarDec("", [])
        no.children.append(Identifier(token.value, []))
        bloco.children.append(no)
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COMMA:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != INT:
            raise Exception("Token errado")
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != NL:
            raise Exception("Token errado")
        self.tokenizer.selectNext()

        token = self.tokenizer.next
        while token.type != EOF:
            bloco.children.append(self.parse_commando())
            token = self.tokenizer.next

        return bloco
    
    def parse_commando(self):
        token = self.tokenizer.next
        if token.type == VIRE:
            no = Virar("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == DIREITA or token.type == ESQUERDA:
                no.value = token.type
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == EM:
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == INT:
                        num = IntVal(token.value, [])
                        no.children.append(num)
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == METROS:
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == EM:
                                self.tokenizer.selectNext()
                                token = self.tokenizer.next
                                if token.type == RUA:
                                    self.tokenizer.selectNext()
                                    token = self.tokenizer.next
                                    if token.type == IDEN:
                                        self.tokenizer.selectNext()
                                        token = self.tokenizer.next
                                        if token.type == NL:
                                            self.tokenizer.selectNext()
                                            return no
                                        raise Exception("Token errado")
                                    raise Exception("Token errado")
                                raise Exception("Token errado")
                            raise Exception("Token errado")
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            raise Exception("Token errado")
        elif token.type == CONTINUE:
            no = Continuar("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == POR:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == INT:
                    num = IntVal(token.value, [])
                    no.children.append(num)
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == METROS:
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == NL:
                            self.tokenizer.selectNext()
                            return no
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            raise Exception("Token errado")
        elif token.type == RUA:
            no = RuaDec("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == IDEN:
                no.children.append(StrVal(token.value, []))
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == ESTA:
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == FECHADA or token.type == ABERTA:
                        estado = token.type
                        no.value = estado
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == NL:
                            self.tokenizer.selectNext()
                            return no
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            raise Exception("Token errado")
        elif token.type == SE:
            no = Se("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == LOCAL:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == MAIOR or token.type == MENOR:
                    no.value = token.type
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == QUE:
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == INT:
                            no.children.append(IntVal(token.value, []))
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == COLON:
                                self.tokenizer.selectNext()
                                token = self.tokenizer.next
                                if token.type == NL:
                                    self.tokenizer.selectNext()
                                    no.children.append(self.parse_bloco())
                                    return no
                                raise Exception("Token errado")
                            raise Exception("Token errado")
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            elif token.type == RUA:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == IDEN:
                    no.children.append(StrVal(token.value, []))
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == ESTA:
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == FECHADA or token.type == ABERTA:
                            estado = token.type
                            no.value = estado
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == COLON:
                                self.tokenizer.selectNext()
                                token = self.tokenizer.next
                                if token.type == NL:
                                    self.tokenizer.selectNext()
                                    no.children.append(self.parse_bloco())
                                    return no
                                raise Exception("Token errado")
                            raise Exception("Token errado")
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            raise Exception("Token errado")
        elif token.type == ENQUANTO:
            no = Enquanto("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == LOCAL:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == MAIOR or token.type == MENOR:
                    no.value = token.type
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == QUE:
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == INT:
                            no.children.append(IntVal(token.value, []))
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == COLON:
                                self.tokenizer.selectNext()
                                token = self.tokenizer.next
                                if token.type == NL:
                                    self.tokenizer.selectNext()
                                    no.children.append(self.parse_bloco())
                                    return no
                                raise Exception("Token errado")
                            raise Exception("Token errado")
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            elif token.type == RUA:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == IDEN:
                    no.children.append(StrVal(token.value, []))
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == ESTA:
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == FECHADA or token.type == ABERTA:
                            estado = token.type
                            no.value = estado
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == COLON:
                                self.tokenizer.selectNext()
                                token = self.tokenizer.next
                                if token.type == NL:
                                    self.tokenizer.selectNext()
                                    no.children.append(self.parse_bloco())
                                    return no
                                raise Exception("Token errado")
                            raise Exception("Token errado")
                        raise Exception("Token errado")
                    raise Exception("Token errado")
                raise Exception("Token errado")
            raise Exception("Token errado")
        raise Exception("Token errado")

    def parse_bloco(self):
        no = Block("", [])
        token = self.tokenizer.next
        while True:
            if token.type != OPTION:
                break
            self.tokenizer.selectNext()
            no.children.append(self.parse_commando())
            token = self.tokenizer.next
        return no

    def run(self, code: str):
        pre_processamento = PrePro()
        codigo_filtrado = pre_processamento.filter(code)

        self.tokenizer = Tokenizer(codigo_filtrado)
        self.tokenizer.selectNext()

        ast = self.parseProgram()

        if self.tokenizer.next.type != EOF:
            raise Exception(f"Token esperado: EOF; Token recebido: {self.tokenizer.next.type}")

        # ast.children.append(FuncCall("main", []))

        return ast

def main():
    parser = Parser()
    if len(sys.argv) < 2:
        raise Exception(f"Para rodar: python main.py arquivo.rota")
    
    with open(sys.argv[1], 'r') as f:
        code = f.readlines()

    code = ''.join(code)

    ast = parser.run(code)
    st = SymbolTable()
    st.create("curr_x", "int")
    st.setter("curr_x", ("int", 350, False))
    st.create("curr_y", "int")
    st.setter("curr_y", ("int", 250, False))
    st.create("curr_dir", "string")
    st.setter("curr_dir", ("string", "x-pos", False))

    plt.savefig(f"./{sys.argv[1]}.png")
    data = image.imread(f"{sys.argv[1]}.png")
    plt.imshow(data)
    ast.Evaluate(st)
    plt.title(f"Desenho para a rota em {sys.argv[1]}")
    plt.savefig(f"./{sys.argv[1]}.png")
    plt.show()

if __name__ == "__main__":
    main()
