%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}

%%

[ \t\n]                 ;
"Rua"                   SAVE_TOKEN; return RUA,
"Partida"               SAVE_TOKEN; return PARTIDA,
"Destino"               SAVE_TOKEN; return DESTINO,
"fechada"               SAVE_TOKEN; return FECHADA,
"aberta"                SAVE_TOKEN; return ABERTA,
"Trajeto"               SAVE_TOKEN; return FUNC,
"Ponto"                 SAVE_TOKEN; return ARG,
"Rotatória"             SAVE_TOKEN; return ROTATORIA,
"Saída"                 SAVE_TOKEN; return SAIDA,
"retorno"               SAVE_TOKEN; return RETORNO,
"Enquanto"              SAVE_TOKEN; return ENQUANTO,
"Se"                    SAVE_TOKEN; return SE,
"mais"                  SAVE_TOKEN; return MAIS,
"menos"                 SAVE_TOKEN; return MENOS,
"maior"                 SAVE_TOKEN; return MAIOR,
"menor"                 SAVE_TOKEN; return MENOR,
"Em"                    SAVE_TOKEN; return EM,
"metros"                SAVE_TOKEN; return METROS,
"vire"                  SAVE_TOKEN; return VIRE,
"direita"               SAVE_TOKEN; return DIREITA,
"esquerda"              SAVE_TOKEN; return ESQUERDA,
"chegará"               SAVE_TOKEN; return CHEGARA,
"está"                  SAVE_TOKEN; return ESTA,
[a-zA-Z_][a-zA-Z0-9_]*  SAVE_TOKEN; return IDEN;
[0-9]+                  SAVE_TOKEN; return INT;
"<"                     return TOKEN(MAIOR);
">"                     return TOKEN(MENOR);
","                     return TOKEN(COMMA);
"+"                     return TOKEN(MAIS);
"-"                     return TOKEN(TOPCAO);
":"                     return TOKEN(COLON);
";"                     return TOKEN(SEMICOLON);
"\n"                    return TOKEN(NL);
.                       printf("Unknown token!n"); yyterminate();

%%