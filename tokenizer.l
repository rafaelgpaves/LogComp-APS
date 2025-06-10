%{
#include "parser.tab.h"
%}

%%

[ \t]                         ;
"Rua"                         { return RUA; }
"Partida"                     { return PARTIDA; }
"Destino"                     { return DESTINO; }
"fechada"                     { return FECHADA; }
"aberta"                      { return ABERTA; }
"Trajeto"                     { return FUNC; }
"Ponto"                       { return ARG; }
"Rotatória"                   { return ROTATORIA; }
"Saída"                       { return SAIDA; }
"retorno"                     { return RETORNO; }
"Enquanto"                    { return ENQUANTO; }
"Se"                          { return SE; }
"mais"                        { return MAIS; }
"menos"                       { return MENOS; }
"maior"                       { return MAIOR; }
"menor"                       { return MENOR; }
"em"                          { return EM; }
"metros"                      { return METROS; }
"Vire"                        { return VIRE; }
"direita"                     { return DIREITA; }
"esquerda"                    { return ESQUERDA; }
"chegará"                     { return CHEGARA; }
"está"                        { return ESTA; }
[A-Z][a-z]*                   { return IDEN; }
[0-9]+                        { return NUMERO; }
","                           { return COMMA; }
"-"                           { return TOPCAO; }
":"                           { return COLON; }
";"                           { return SEMICOLON; }
\n                            { return NL; }
.                             { printf("Unknown token!\n"); yyterminate(); }

%%