%{
    #include <stdio.h>
%}

%token RUA PARTIDA DESTINO FECHADA ABERTA ENQUANTO SE EM METROS VIRE DIREITA ESQUERDA ESTA
%token COLON COMMA 
%token IDEN NUMERO
%token NL EOL
%token FUNC ARG ROTATORIA SAIDA RETORNO CHEGARA MAIS MENOS MAIOR MENOR TOPCAO SEMICOLON

%%

sintaxe: 
    PARTIDA COLON RUA IDEN COMMA NUMERO NL DESTINO COLON RUA IDEN COMMA NUMERO NL direcoes
    ;

direcoes: 
    comando 
    | direcoes comando
    ;

comando: atribuicao | virar | se | enquanto;

bloco:
    NL TOPCAO comando
    | bloco TOPCAO comando

atribuicao: RUA IDEN ESTA estado NL;

virar: VIRE direcao EM NUMERO METROS EM RUA IDEN NL;

se: SE condicao COLON bloco;

enquanto: ENQUANTO condicao COLON bloco;

condicao: RUA IDEN ESTA estado;

direcao: DIREITA | ESQUERDA;

estado: ABERTA | FECHADA;

%%

int main(int argc, char **argv)
{
    yyparse();

    return 0;
}

yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
}
