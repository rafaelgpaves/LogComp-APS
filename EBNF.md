SINTAXE = "Partida: " RUA \n "Destino: " RUA \n DIREÇÕES

DIREÇÕES = {COMANDO}+

COMANDO = ATRIB | CONTINUAR | VIRAR | SE | ENQUANTO

BLOCO = {\n "-" COMANDO}+

ATRIB = nome-rua " está " [aberta|fechada]

CONTINUAR = "Continue por " numero " metros"

VIRAR = "Vire " [direita|esquerda] " em " numero " metros em " nome-rua

SE = "Se " cond ":" BLOCO

ENQUANTO = "Enquanto " cond ":" BLOCO

cond = {nome-rua " está " [aberta|fechada]} | {" local " [maior|menor] que numero}

RUA = nome-rua, numero

nome-rua = "Rua" {" " letra-maiuscula {letra}*}+

letra-maiuscula = "A"..."Z"

letra = "a"..."z"

numero = {digito}+

digito = "0"..."9"
