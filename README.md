# Rota

Rota é uma linguagem de programação simples, desenvolvida com o intuito de transformar instruções de caminhos, como vistas em lugares como *Mapas* ou *Google Maps*, em desenhos para visualização fácil do percurso.

Uma das motivações do desenvolvimento dessa linguagem foi minha falta de conhecimento das ruas e caminhos de Sâo Paulo. Sempre me vejo olhando rotas em aplicativos, achei que seria interessante poder visualizar isso facilmente.

Feito como APS para a disciplina de Lógica da Computação, 7o semestre de Engenharia da Computação do Insper.

## EBNF

Veja o [EBNF](EBNF.md)

## Características da linguagem

- "Variáveis" no formato de ruas
    - Cada Rua deve ter apenas uma palavra como nome
- Condicionais
    - Rua esta aberta ou fechada
    - Posição atual é menor ou maior do que um numero
- Se (if) e enquanto (while)
- Output: desenho da rota, mostrado de dois jeitos
    - Após rodar, ele é mostrado automaticamente
    - É salvo num arquivo .png, com o mesmo nome do arquivo de entrada

Veja os exemplos [aqui](./examples/)
