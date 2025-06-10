flex_bison: tokenizer.l parser.y
	bison -d parser.y
	flex tokenizer.l
	cc -o $@ parser.tab.c lex.yy.c -lfl