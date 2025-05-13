%type <dval> expression

%%

sintaxe: PARTIDA COLON RUA IDEN NL DESTINO COLON RUA IDEN NL direcoes

direcoes: comando NL | direcoes comando NL

comando: atribuicao | se | enquanto

atribuicao: RUA IDEN ESTA ABERTA | FECHADA

se: SE condicao comando

enquanto: ENQUANTO condicao comando

condicao: NUMERO MAIOR | MENOR NUMERO

%%
