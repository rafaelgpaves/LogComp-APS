%{
    #include <stdio.h>
%}

%token RUA PARTIDA DESTINO FECHADA ABERTA ENQUANTO SE EM METROS VIRE DIREITA ESQUERDA ESTA MAIOR MENOR CONTINUE POR LOCAL QUE
%token COLON COMMA TOPCAO
%token IDEN NUMERO
%token NL EOL

%%

sintaxe: 
    PARTIDA COLON RUA IDEN COMMA NUMERO NL DESTINO COLON RUA IDEN COMMA NUMERO NL direcoes
    ;

direcoes: 
    comando 
    | direcoes comando
    ;

comando: atribuicao | continuar | virar | se | enquanto;

bloco:
    NL TOPCAO comando
    | bloco TOPCAO comando

atribuicao: RUA IDEN ESTA estado NL;

continuar: CONTINUE POR NUMERO METROS NL;

virar: VIRE direcao EM NUMERO METROS EM RUA IDEN NL;

se: SE condicao COLON bloco;

enquanto: ENQUANTO condicao COLON bloco;

condicao: 
    RUA IDEN ESTA estado
    | LOCAL relacao QUE NUMERO
    ;

direcao: DIREITA | ESQUERDA;

estado: ABERTA | FECHADA;

relacao: MAIOR | MENOR

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
