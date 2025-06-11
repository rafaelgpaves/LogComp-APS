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
"Continue"                    { return CONTINUE; }
"por"                         { return POR; }
"local"                       { return LOCAL; }
"que"                         { return QUE; }
"Enquanto"                    { return ENQUANTO; }
"Se"                          { return SE; }
"maior"                       { return MAIOR; }
"menor"                       { return MENOR; }
"em"                          { return EM; }
"metros"                      { return METROS; }
"Vire"                        { return VIRE; }
"direita"                     { return DIREITA; }
"esquerda"                    { return ESQUERDA; }
"esta"                        { return ESTA; }
[a-zA-z]+                     { return IDEN; }
[0-9]+                        { return NUMERO; }
","                           { return COMMA; }
"-"                           { return TOPCAO; }
":"                           { return COLON; }
\n                            { return NL; }
.                             { printf("Unknown token!\n"); yyterminate(); }

%%