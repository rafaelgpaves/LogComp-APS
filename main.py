from tokens import COLON, COMMA, EOF, IDEN, INT, KEYWORDS, NL, OPTION, SEMICOLON

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
    