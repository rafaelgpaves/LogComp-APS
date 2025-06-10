RUA = "rua"
IDEN = "identifier"
PARTIDA = "partida"
DESTINO = "destino"
FECHADA = "fechada"
ABERTA = "aberta"
INT = "int"
FUNC = "function"
ARG = "argument"
COMMA = ","
COLON = ":"
SEMICOLON = ";"
ROTATORIA = "rotatoria"
SAIDA = "saida"
OPTION = "-"
RETORNO = "retorno"
ENQUANTO = "enquanto"
SE = "se"
MAIS = "mais"
MENOS = "menos"
MAIOR = "maior"
MENOR = "menor"
EM = "em"
METROS = "metros"
VIRE = "vire"
DIREITA = "direita"
ESQUERDA = "esquerda"
CHEGARA = "chegará"
ESTA = "esta"
NL = "newline"
EOF = ""

KEYWORDS = {
    "Rua": RUA,
    "Partida": PARTIDA,
    "Destino": DESTINO,
    "fechada": FECHADA,
    "aberta": ABERTA,
    "Trajeto": FUNC,
    "Ponto": ARG,
    "Rotatória": ROTATORIA,
    "Saída": SAIDA,
    "retorno": RETORNO,
    "Enquanto": ENQUANTO,
    "Se": SE,
    "mais": MAIS,
    "menos": MENOS,
    "maior": MAIOR,
    "menor": MENOR,
    "em": EM,
    "metros": METROS,
    "Vire": VIRE,
    "direita": DIREITA,
    "esquerda": ESQUERDA,
    "chegará": CHEGARA,
    "esta": ESTA,
}

VAR = "var"
TYPE = "type"
INT = "int"
BOOL = "bool"
STR = "string"
PLUS = "+"
MINUS = "-"
MULT = "*"
DIV = "/"
OR = "||"
AND = "&&"
NOT = "!"
MORE = ">"
LESS = "<"
EQUAL = "=="
COMMA = ","
FOR = "for"
IF = "if"
ELSE = "else"
READ = "read"
OPENPAR = "("
CLOSEPAR = ")"
REC = "="
IDEN = "identifier"
PRINT = "print"
NL = r"\n"
OPENKEY = "{"
CLOSEKEY = "}"
FUNC = "func"
RETURN = "return"
EOF = ""

# KEYWORDS = {
#     "Println": PRINT,
#     "for": FOR,
#     "if": IF,
#     "else": ELSE,
#     "Scan": READ,
#     "var": VAR,
#     "func": FUNC,
#     "return": RETURN
# }

TYPES = {
    "int": TYPE,
    "string": TYPE,
    "bool": TYPE
}

BOOLEANS = {
    "false": False,
    "true": True
}
