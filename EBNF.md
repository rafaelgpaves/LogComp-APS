SINTAXE = "Partida: " RUA \n "Destino: " RUA \n DIREÇÕES

DIREÇÕES = {COMANDO}+

COMANDO = ATRIB | CONTINUAR | VIRAR | SE | ENQUANTO

BLOCO = {\n "-" COMANDO}+

ATRIB = nome-rua " está " [aberta|fechada]

CONTINUAR = "Continue por " numero " metros"

VIRAR = "Vire " [direita|esquerda] " em " numero " metros em " nome-rua

SE = "Se " nome-rua " está " [aberta|fechada] ":" BLOCO

ENQUANTO = "Enquanto " nome-rua " está " [aberta|fechada] ":" BLOCO

RUA = nome-rua, numero

nome-rua = "Rua" {" " letra-maiuscula {letra}*}+

letra-maiuscula = "A"..."Z"

letra = "a"..."z"

numero = {digito}+

digito = "0"..."9"
