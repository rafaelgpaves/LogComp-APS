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
                
                if self.next.value in TYPES:
                    tipo = self.next.value
                    self.next = Token(TYPE)
                    self.next.value = tipo
                    return
                
                if self.next.value in BOOLEANS:
                    self.next = Token(BOOL)
                    return
                
                if self.position == len(self.source):
                    return
                
            if self.next.value in KEYWORDS:
                self.next = Token(KEYWORDS[self.next.value])
                return
        
            if self.next.value in TYPES:
                tipo = self.next.value
                self.next = Token(TYPE)
                self.next.value = tipo

            if self.next.value in BOOLEANS:
                self.next = Token(BOOL)
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

        if self.source[self.position] == "*":
            self.next = Token(MULT)
            self.position += 1
            return
        elif self.source[self.position] == "/":
            self.next = Token(DIV)
            self.position += 1
            return
        elif self.source[self.position] == "+":
            self.next = Token(PLUS)
            self.position += 1
            return
        elif self.source[self.position] == "-":
            self.next = Token(OPTION)
            self.position += 1
            return
        elif self.source[self.position] == "(":
            self.next = Token(OPENPAR)
            self.position += 1
            return
        elif self.source[self.position] == ")":
            self.next = Token(CLOSEPAR)
            self.position += 1
            return
        elif self.source[self.position] == "{":
            self.next = Token(OPENKEY)
            self.position += 1
            return
        elif self.source[self.position] == "}":
            self.next = Token(CLOSEKEY)
            self.position += 1
            return
        elif self.source[self.position] == "\n":
            self.next = Token(NL)
            self.position += 1
            return
        elif self.source[self.position] == "=":
            self.position += 1
            if self.source[self.position] == "=":
                self.next = Token(EQUAL)
                self.position += 1
                return
            self.next = Token(REC)
            return
        elif self.source[self.position] == "!":
            self.next = Token(NOT)
            self.position += 1
            return
        elif self.source[self.position] == "<":
            self.next = Token(LESS)
            self.position += 1
            return
        elif self.source[self.position] == ">":
            self.next = Token(MORE)
            self.position += 1
            return
        elif self.source[self.position] == "|":
            self.position += 1
            if self.source[self.position] == "|":
                self.next = Token(OR)
                self.position += 1
                return
        elif self.source[self.position] == "&":
            self.position += 1
            if self.source[self.position] == "&":
                self.next = Token(AND)
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

    def parseBlock(self):

        token = self.tokenizer.next
        if token.type == OPENKEY:
            self.tokenizer.selectNext()
            token = self.tokenizer.next

            if token.type == NL:
                self.tokenizer.selectNext()
                token = self.tokenizer.next

                no_block = Block("", [])
                while token.type != CLOSEKEY:
                    statement = self.parseStatement()
                    no_block.children.append(statement)
                    token = self.tokenizer.next

                self.tokenizer.selectNext()
                return no_block
            
            raise Exception(f"Token esperado: NL (nova linha); Token recebido: {token.type}")
        raise Exception(f"Token esperado: OPENKEY; Token recebido: {token.type}")

    def parseStatement(self):
        token = self.tokenizer.next
        if token.type == NL:
            self.tokenizer.selectNext()
            return NoOp("", [])

        elif token.type == IDEN:
            resultado = token.value
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == REC:
                no = Identifier(resultado, [])
                self.tokenizer.selectNext()
                no = Assignment("", [no, self.parseBExpression()])
                token = self.tokenizer.next
                if token.type == NL:
                    self.tokenizer.selectNext()
                    return no
                raise Exception(f"Token esperado: NL (nova linha); Token recebido: {token.type}")
            if token.type == OPENPAR:
                no = FuncCall(resultado, [])
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                while token.type != CLOSEPAR:
                    no.children.append(self.parseBExpression())
                    token = self.tokenizer.next
                    if token.type == CLOSEPAR:
                        break
                    elif token.type == COMMA:
                        self.tokenizer.selectNext()
                    else:
                        raise Exception(f"Token esperado: COMMA, CLOSEPAR; Token recebido: {token.type}")
                    token = self.tokenizer.next
                self.tokenizer.selectNext()
                return no
            raise Exception(f"Token esperado: REC, OPENPAR; Token recebido: {token.type}")
        
        elif token.type == VAR:
            resultado = token.value
            no = VarDec("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == IDEN:
                no.children.append(Identifier(token.value, []))
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == TYPE:
                    no.value = token.value
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == REC:
                        self.tokenizer.selectNext()
                        no.children.append(self.parseBExpression())
                    return no
                raise Exception(f"Token esperado: INT, STR, BOOL; Token recebido: {token.type}")
            raise Exception(f"Token esperado: IDEN; Token recebido: {token.type}") 
        
        elif token.type == PRINT:
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == OPENPAR:
                self.tokenizer.selectNext()
                no = self.parseBExpression()
                token = self.tokenizer.next
                if token.type == CLOSEPAR:
                    self.tokenizer.selectNext()
                    no = Print("", [no])
                    token = self.tokenizer.next
                    if token.type == NL:
                        self.tokenizer.selectNext()
                        return no
                    raise Exception(f"Token esperado: NL (nova linha); Token recebido: {token.type}")
                raise Exception(f"Token esperado: CLOSEPAR; Token recebido: {token.type}")
            raise Exception(f"Token esperado: OPENPAR; Token recebido: {token.type}")
        
        elif token.type == FOR:
            self.tokenizer.selectNext()
            no = While("", [])
            no.children.append(self.parseBExpression())
            no.children.append(self.parseBlock())
            return no
        
        elif token.type == IF:
            self.tokenizer.selectNext()
            no = If("", [])
            no.children.append(self.parseBExpression())
            no.children.append(self.parseBlock())
            token = self.tokenizer.next
            if token.type == ELSE:
                self.tokenizer.selectNext()
                no.children.append(self.parseBlock())
            return no
        
        elif token.type == RETURN:
            self.tokenizer.selectNext()
            no = Return("", [])
            no.children.append(self.parseBExpression())
            return no
        
        no = self.parseBlock()
        return no
    
    def parseFuncDec(self):
        no = FuncDec("", [])
        token = self.tokenizer.next
        if token.type == FUNC:
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == IDEN:
                no.children.append(Identifier(token.value, []))
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == OPENPAR:
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    while token.type != CLOSEPAR:
                        if token.type == IDEN:
                            argumento = VarDec("", [])
                            argumento.children.append(Identifier(token.value, []))
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == TYPE:
                                argumento.value = token.value
                                self.tokenizer.selectNext()
                                no.children.append(argumento)
                                token = self.tokenizer.next
                                if token.type == CLOSEPAR:
                                    token = self.tokenizer.next
                                    break
                                elif token.type == COMMA:
                                    self.tokenizer.selectNext()
                                    token = self.tokenizer.next
                                else:
                                    raise Exception(f"Token esperado: COMMA, CLOSEPAR; Token recebido: {token.type}")
                            else:    
                                raise Exception(f"Token esperado: TYPE; Token recebido: {token.type}")
                        else:
                            raise Exception(f"Token esperado: IDEN, CLOSEPAR; Token recebido: {token.type}")
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == TYPE:
                        no.value = token.value
                        self.tokenizer.selectNext()
                    no.children.append(self.parseBlock())
                    return no
                raise Exception(f"Token esperado: OPENPAR; Token recebido: {token.type}")
            raise Exception(f"Token esperado: IDEN; Token recebido: {token.type}")
        raise Exception(f"Token esperado: FUNC; Token recebido: {token.type}")
    
    def parseVarDec(self):
        token = self.tokenizer.next
        if token.type == RUA:
            token = self.tokenizer.next
            no = VarDec("", [])
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == IDEN:
                no.children.append(Identifier(token.value, []))
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == ESTA:
                    no.value = "int"
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == REC:
                        self.tokenizer.selectNext()
                        no.children.append(self.parseBExpression())
                    return no
                raise Exception(f"Token esperado: INT, STR, BOOL; Token recebido: {token.type}")
            raise Exception(f"Token esperado: IDEN; Token recebido: {token.type}") 
        raise Exception(f"Token esperado: VAR; Token recebido: {token.type}") 
    
    def parseBExpression(self):
        no = self.parseBTerm()
        token = self.tokenizer.next
        while token.type == OR:
            self.tokenizer.selectNext()
            no = BinOp(OR, [no, self.parseBTerm()])
            token = self.tokenizer.next

        return no
    
    def parseBTerm(self):
        no = self.parseRelExpression()
        token = self.tokenizer.next
        while token.type == AND:
            self.tokenizer.selectNext()
            no = BinOp(AND, [no, self.parseRelExpression()])
            token = self.tokenizer.next

        return no
    
    def parseRelExpression(self):
        no = self.parseExpression()
        token = self.tokenizer.next
        while token.type == EQUAL or token.type == MORE or token.type == LESS:
            
            if token.type == EQUAL:
                self.tokenizer.selectNext()
                no = BinOp(EQUAL, [no, self.parseExpression()])
            if token.type == MORE:
                self.tokenizer.selectNext()
                no = BinOp(MORE, [no, self.parseExpression()])
            if token.type == LESS:
                self.tokenizer.selectNext()
                no = BinOp(LESS, [no, self.parseExpression()])
            token = self.tokenizer.next

        return no

    def parseExpression(self):
        no = self.parseTerm()
        token = self.tokenizer.next
        while token.type == PLUS or token.type == MINUS:
            
            if token.type == PLUS:
                self.tokenizer.selectNext()
                no = BinOp(PLUS, [no, self.parseTerm()])
            elif token.type == MINUS:
                self.tokenizer.selectNext()
                no = BinOp(MINUS, [no, self.parseTerm()])
            token = self.tokenizer.next
                
        return no
    
    def parseTerm(self):
        no = self.parseFactor()
        token = self.tokenizer.next
        while token.type == MULT or token.type == DIV:
            
            if token.type == MULT:
                self.tokenizer.selectNext()
                no = BinOp(MULT, [no, self.parseFactor()])
            elif token.type == DIV:
                self.tokenizer.selectNext()
                no = BinOp(DIV, [no, self.parseFactor()])
            token = self.tokenizer.next
                
        return no
    
    def parseFactor(self):
        token = self.tokenizer.next
        if token.type == INT:
            resultado = token.value
            no = IntVal(resultado, [])
            self.tokenizer.selectNext()
            return no
        elif token.type == IDEN:
            resultado = token.value
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == OPENPAR:
                no = FuncCall(resultado, [])
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                while token.type != CLOSEPAR:
                    no.children.append(self.parseBExpression())
                    token = self.tokenizer.next
                    if token.type == CLOSEPAR:
                        break
                    elif token.type == COMMA:
                        self.tokenizer.selectNext()
                    else:
                        raise Exception(f"Token esperado: COMMA, CLOSEPAR; Token recebido: {token.type}")
                    token = self.tokenizer.next
                self.tokenizer.selectNext()
                return no
            no = Identifier(resultado, [])
            return no
        elif token.type == STR:
            resultado = token.value
            no = StrVal(resultado, [])
            self.tokenizer.selectNext()
            return no
        elif token.type == BOOL:
            resultado = token.value
            no = BoolVal(resultado, [])
            self.tokenizer.selectNext()
            return no
        elif token.type == PLUS:
            self.tokenizer.selectNext()
            no = UnOp(PLUS, [self.parseFactor()])
            return no
        elif token.type == MINUS:
            self.tokenizer.selectNext()
            no = UnOp(MINUS, [self.parseFactor()])
            return no
        elif token.type == NOT:
            self.tokenizer.selectNext()
            no = UnOp(NOT, [self.parseFactor()])
            return no
        elif token.type == OPENPAR:
            self.tokenizer.selectNext()
            no = self.parseBExpression()
            token = self.tokenizer.next
            if token.type == CLOSEPAR:
                self.tokenizer.selectNext()
                return no
            raise Exception(f"Token esperado: CLOSEPAR; Token recebido: {token.type}")
        elif token.type == READ:
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == OPENPAR:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == CLOSEPAR:
                    self.tokenizer.selectNext()
                    no = Read("", [])
                    return no
                raise Exception(f"Token esperado: CLOSEPAR; Token recebido: {token.type}")
            raise Exception(f"Token esperado: OPENPAR; Token recebido: {token.type}")
        raise Exception(f"Token {token.type} não esperado; Tokens esperados: INT, IDEN, PLUS, MINUS, NOT, OPENPAR, READ")

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
