# APS

APS para a disciplina de Lógica da Computação, 7o semestre de Engenharia da Computação do Insper

## EBNF

Veja o [EBNF](EBNF.md)

## Linguagem

Consiste em pegar uma rota de carro de um local para outro.

Ouptut: Mostrar um mapa em uma grade quadriculada com o percurso

### Exemplo:

Partida: Rua X, 1000

Destino: Rua Z, 10000

Rua Y está fechada em 1500

Em 100 metros, vire a direita em Rua Y

Enquanto numero de Rua Y menor que 1500:
- Destino: Rua Z, numero Destino mais 100
- Continue por 100 metros

Se Rua Y fechada em numero Atual, pegue a rotatoria na 1a saida

Rotatoria:
- Saida 1: vire a direita em Rua Z; em 8 kilômetros, você chegará em Destino
- Saida padrão: vire a esquerda em Rua Z; em 1000 metros, faça o retorno; em 9 kilômetros, você chegará em Destino

### Função:

Trajeto PegarParalela:

Ponto Rua 1, 100

Ponto Rua 2, 200

Em 100 metros, vire a direta em Rua 1

Em 10 metros, vire a esquerda em Rua 2

Em 100 metros, continue em frente

Chegada Rua 2, 200

Trajeto Principal:

Partida: Rua X, 110

Destino: Rua Z, 3000

Em 100 metros, vire à direita em Rua Y

PegarParalela Rua X, Rua Y

Em 350 metros, vire a esquerda em Rua Z

Em 2000 metros, você chegará em Rua Z, 10000

