SINTAXE = "Partida: " RUA\n DIREÇÕES "Destino: " RUA

DIREÇÕES = COMANDO \n

COMANDO = "Em " numero " metros," AÇÃO " em " RUA

AÇÃO = virar | rotatõria | continuar

RUA = nome-rua, numero

nome-rua = "Rua" {" " letra-maiuscula {letra}*}+

letra-maiuscula = "A"..."Z"

letra = "a"..."z"

numero = {digito}+

digito = "0"..."9"
