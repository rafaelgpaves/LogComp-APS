from tokens import ABERTA, COLON, COMMA, DESTINO, DIREITA, EM, ENQUANTO, EOF, ESQUERDA, ESTA, FECHADA, IDEN, INT, KEYWORDS, MAIOR, MAIS, MENOR, MENOS, METROS, NL, OPTION, PARTIDA, ROTATORIA, RUA, SE, SEMICOLON, VIRE

class Token:
    def __init__(self, tipo: str):
        self.type: str = tipo
        self.value: int = 0

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
                
            if self.next.value in KEYWORDS:
                self.next = Token(KEYWORDS[self.next.value])
                return

        if self.source[self.position] == ":":
            self.next = Token(COLON)
            self.position += 1
            return
        elif self.source[self.position] == ";":
            self.next = Token(SEMICOLON)
            self.position += 1
            return
        elif self.source[self.position] == ",":
            self.next = Token(COMMA)
            self.position += 1
            return
        elif self.source[self.position] == "-":
            self.next = Token(OPTION)
            self.position += 1
            return
        elif self.source[self.position] == "\n":
            self.next = Token(NL)
            self.position += 1
            return
        raise Exception(f"Letra \"{self.source[self.position]}\" não existente")
    
class Parser:
    def __init__(self):
        self.tokenizer: Tokenizer

    def parse_code(self):
        token = self.tokenizer.next
        if token.type != PARTIDA:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COLON:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != RUA:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != NL:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != DESTINO:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != COLON:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != RUA:
            raise Exception()
        self.tokenizer.selectNext()
        token = self.tokenizer.next
        if token.type != NL:
            raise Exception()
        self.tokenizer.selectNext()

        return self.parse_direcao()

    def parse_direcao(self):
        self.parse_comando()
        token = self.tokenizer.next
        if token.type != NL:
            raise Exception()
        
    def parse_comando(self):
        token = self.tokenizer.next
        if token.type == RUA:
            self.tokenizer.selectNext()
            token = self.tokenizer.next
            if token.type == ESTA:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == FECHADA or token.type == ABERTA:
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                raise Exception()
            raise Exception()
        elif token.type == EM:
            self.tokenizer.selectNext()
            if token.type == INT:
                self.tokenizer.selectNext()
                token = self.tokenizer.next
                if token.type == METROS:
                    self.tokenizer.selectNext()
                    token = self.tokenizer.next
                    if token.type == COMMA: 
                        self.tokenizer.selectNext()
                        token = self.tokenizer.next
                        if token.type == VIRE:
                            self.tokenizer.selectNext()
                            token = self.tokenizer.next
                            if token.type == DIREITA or token.type == ESQUERDA:
                                self.tokenizer.selectNext()
                            raise Exception()
                        raise Exception()
                    raise Exception()
                raise Exception()
            raise Exception()
        elif token.type == SE:
            self.tokenizer.selectNext()
            self.parse_rel_expression()
            self.parse_direcao()
        elif token.type == ENQUANTO:
            self.tokenizer.selectNext()
            self.parse_rel_expression()
            self.parse_direcao()
        elif token.type == ROTATORIA:
            self.tokenizer.selectNext()
            self.parse_rel_expression()
            self.parse_direcao()
        raise Exception()
    
    def parse_rel_expression(self):
        self.parse_expression()
        token = self.tokenizer.next
        while token.type == MAIOR or token.type == MENOR:
            
            if token.type == MAIOR:
                self.tokenizer.selectNext()
            if token.type == MENOR:
                self.tokenizer.selectNext()
            token = self.tokenizer.next

    def parse_expression(self):
        no = self.parse_factor()
        token = self.tokenizer.next
        while token.type == MAIS or token.type == MENOS:
            
            if token.type == MAIS:
                self.tokenizer.selectNext()
            elif token.type == MENOS:
                self.tokenizer.selectNext()
            token = self.tokenizer.next
                
        return no
    
    def parse_factor(self):
        token = self.tokenizer.next
        if token.type == INT:
            self.tokenizer.selectNext()
        elif token.type == IDEN:
            self.tokenizer.selectNext()
        raise Exception()
